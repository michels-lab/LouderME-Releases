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


def main() -> int:
    shell = shell_body()
    assert_publisher_shell(shell)
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
    print("PASS: publisher Bash syntax, tag guards, and six immutable-asset test cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
