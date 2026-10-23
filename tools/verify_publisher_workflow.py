#!/usr/bin/env python3
"""Offline fail-closed tests for the dedicated LouderMe unified publisher.

Never downloads or publishes binaries. Exercises the exact existing-tag digest
guard extracted from the real workflow, so tests track production logic.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/publish-louderme-unified.yml"


def shell_body() -> str:
    lines = WORKFLOW.read_text(encoding="utf-8").splitlines()
    starts = [i for i, line in enumerate(lines) if line == "        run: |"]
    if len(starts) != 1:
        raise AssertionError("Expected exactly one publisher run: | block")
    output: list[str] = []
    for line in lines[starts[0] + 1 :]:
        if not line.strip():
            output.append("")
        elif line.startswith("          "):
            output.append(line[10:])
        else:
            break
    if not output:
        raise AssertionError("Publisher Bash body is empty")
    return "\n".join(output) + "\n"


def assert_publisher_shell(shell: str) -> None:
    check = subprocess.run(["bash", "-n"], input=shell, text=True, capture_output=True)
    if check.returncode:
        raise AssertionError("Publisher Bash invalid: " + check.stderr)
    for required in (
        '[[ "$AV" =~ ^[0-9]+\\.[0-9]+\\.[0-9]+$ ]]',
        '[[ "$WV" =~ ^[0-9]+\\.[0-9]+\\.[0-9]+$ ]]',
        '[[ "$AVC" =~ ^[1-9][0-9]*$ ]]',
        '[[ "$WINDOWS_SOURCE_SHA" =~ ^[0-9a-f]{40}$ ]]',
        'if [[ "$WINDOWS_TAG_SHA" != "$WINDOWS_SOURCE_SHA" ]]; then',
        'sha256sum -c "LouderMe-Setup-v$WV.exe.sha256"',
        'sha256sum -c "LouderMe-Portable-v$WV.exe.sha256"',
    ):
        if required not in shell:
            raise AssertionError("Publisher security guard missing: " + required)
    if "--clobber" in shell and "Never --clobber" not in shell:
        raise AssertionError("Publisher must not overwrite previously published assets")
    if "gh release upload " in shell:
        raise AssertionError("Publisher must never re-upload to existing release")


def existing_release_guard(shell: str) -> str:
    start = "python3 - <<'PY'\n"
    if start not in shell:
        raise AssertionError("Existing release SHA guard not found")
    return shell.split(start, 1)[1].split("\nPY\n", 1)[0]


def run_fixture(code: str, *, mutation: str) -> subprocess.CompletedProcess[str]:
    names = (
        "LouderMe-v0.1.12-sideload.apk",
        "LouderMe-v0.1.12-sideload.apk.sha256",
        "LouderMe-Setup-v0.1.12.exe",
        "LouderMe-Setup-v0.1.12.exe.sha256",
        "LouderMe-Portable-v0.1.12.exe",
        "LouderMe-Portable-v0.1.12.exe.sha256",
    )
    with tempfile.TemporaryDirectory(prefix="louderme-release-qa-") as tmp:
        base = Path(tmp)
        folder = base / "dist"
        folder.mkdir()
        for name in names:
            (folder / name).write_bytes(name.encode("utf-8"))
        assets = [
            {"name": name, "digest": "sha256:" + hashlib.sha256(name.encode("utf-8")).hexdigest()}
            for name in names
        ]
        release = {"draft": False, "prerelease": False, "assets": assets}
        if mutation == "different-digest":
            release["assets"][0]["digest"] = "sha256:" + "0" * 64
        elif mutation == "missing-asset":
            release["assets"].pop()
        elif mutation == "extra-asset":
            release["assets"].append({"name": "unexpected", "digest": "sha256:" + "0" * 64})
        elif mutation == "draft":
            release["draft"] = True
        elif mutation == "duplicate-name":
            release["assets"][1]["name"] = release["assets"][0]["name"]
        elif mutation != "matching":
            raise ValueError(mutation)
        (base / "existing-release.json").write_text(json.dumps(release), encoding="utf-8")
        return subprocess.run(
            [sys.executable, "-c", code], cwd=base, text=True, capture_output=True,
        )


def verified_push_function(shell: str) -> str:
    """Use production's exact Bash retry function, not a duplicated mock."""
    marker = "push_verified_updater_feeds() {\n"
    if shell.count(marker) != 1:
        raise AssertionError("Expected exactly one verified feed push function")
    start = shell.index(marker)
    end = shell.find("\n}\n", start)
    if end == -1:
        raise AssertionError("Verified feed function is unterminated")
    return shell[start : end + 3] + "\n"


def run_git(*args: str, cwd: Path | None = None) -> str:
    command = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True
    )
    if command.returncode:
        raise AssertionError(
            f"git {args} failed: {command.stdout} {command.stderr}"
        )
    return command.stdout.strip()


def test_concurrent_manifest_push(shell: str, *, conflicting: bool) -> None:
    """Real, offline Git race: disjoint audit succeeds; conflicting feed fails."""
    with tempfile.TemporaryDirectory(prefix="louderme-git-push-") as tmp:
        root = Path(tmp)
        remote = root / "remote.git"
        run_git("init", "--bare", "--initial-branch=main", str(remote))
        seed = root / "seed"
        run_git("clone", str(remote), str(seed))
        run_git("config", "user.email", "seed@example.invalid", cwd=seed)
        run_git("config", "user.name", "QA Seed", cwd=seed)
        (seed / "louderme").mkdir()
        (seed / "louderme-desktop").mkdir()
        (seed / "docs").mkdir()
        (seed / "louderme/latest.json").write_text("android-v0.1.12\n")
        (seed / "louderme-desktop/latest.json").write_text("windows-v0.1.13\n")
        (seed / "docs/audit.md").write_text("initial audit\n")
        run_git("add", ".", cwd=seed)
        run_git("commit", "-m", "initial", cwd=seed)
        run_git("push", "origin", "main", cwd=seed)

        pub, steward = root / "publisher", root / "steward"
        for clone in (pub, steward):
            run_git("clone", str(remote), str(clone))
            run_git("config", "user.email", "qa@example.invalid", cwd=clone)
            run_git("config", "user.name", "QA Publisher", cwd=clone)

        # The publisher's verified source release was not yet pushed.
        (pub / "louderme/latest.json").write_text("android-v0.1.12-new-url\n")
        (pub / "louderme-desktop/latest.json").write_text("windows-v0.1.14\n")
        run_git("add", "louderme/latest.json", "louderme-desktop/latest.json", cwd=pub)
        run_git("commit", "-m", "validated released manifests", cwd=pub)

        if conflicting:
            (steward / "louderme-desktop/latest.json").write_text(
                "windows-v0.1.15-unrelated\n"
            )
        else:
            (steward / "docs/audit.md").write_text("new independent audit\n")
        run_git("add", ".", cwd=steward)
        run_git("commit", "-m", "concurrent auditor", cwd=steward)
        audit_sha = run_git("rev-parse", "HEAD", cwd=steward)
        run_git("push", "origin", "main", cwd=steward)

        executed = subprocess.run(
            ["bash", "-c", verified_push_function(shell)
             + "\npush_verified_updater_feeds\n"],
            cwd=pub, capture_output=True, text=True, timeout=30,
        )
        remote_desktop = run_git(
            "--git-dir", str(remote), "show",
            "main:louderme-desktop/latest.json",
        )
        remote_android = run_git(
            "--git-dir", str(remote), "show", "main:louderme/latest.json"
        )
        remote_audit = run_git(
            "--git-dir", str(remote), "show", "main:docs/audit.md"
        )
        main_sha = run_git("--git-dir", str(remote), "rev-parse", "main")
        run_git(
            "--git-dir", str(remote), "merge-base",
            "--is-ancestor", audit_sha, main_sha
        )
        if conflicting:
            if executed.returncode == 0 or remote_desktop != "windows-v0.1.15-unrelated":
                raise AssertionError(
                    "Conflicting/stale publisher silently rewrote a newer updater feed"
                )
            if remote_android != "android-v0.1.12":
                raise AssertionError("Conflicting release partially changed the Android feed")
        else:
            if (executed.returncode != 0
                    or remote_desktop != "windows-v0.1.14"
                    or remote_android != "android-v0.1.12-new-url"
                    or remote_audit != "new independent audit"):
                raise AssertionError(
                    f"Disjoint File Steward commit blocked verified release recovery: "
                    f"{executed.stdout} {executed.stderr}"
                )


def main() -> int:
    shell = shell_body()
    assert_publisher_shell(shell)
    for required in (
        "git push origin HEAD:refs/heads/main",
        "git fetch --no-tags origin main",
        "git rebase FETCH_HEAD",
        "git rebase --abort",
    ):
        if required not in shell:
            raise AssertionError("Fail-closed concurrent publish recovery missing: " + required)
    test_concurrent_manifest_push(shell, conflicting=False)
    test_concurrent_manifest_push(shell, conflicting=True)
    guard = existing_release_guard(shell)
    for mutation, allowed in (
        ("matching", True),
        ("different-digest", False),
        ("missing-asset", False),
        ("extra-asset", False),
        ("draft", False),
        ("duplicate-name", False),
    ):
        result = run_fixture(guard, mutation=mutation)
        if (result.returncode == 0) != allowed:
            raise AssertionError(
                f"Fixture {mutation} got rc={result.returncode}; "
                f"stdout={result.stdout}; stderr={result.stderr}"
            )
    print("PASS: publisher Bash, immutable-asset guards, concurrent audit recovery, and manifest conflict rejection")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
