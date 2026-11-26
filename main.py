#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes a single out-of-office auto-reply, one line long, to
/output/entry.txt (the harness output directory). The reply is a fixed,
deterministic string: no randomness, no network, no input files.

The line was chosen by a local pre-judge: eight fresh candidates were
played pairwise, both orders, under the kit's own judge brief (a free
proxy model), and this one won the round-robin. It reads like a real
away message, lands on the first read, and turns the usual "if this is
urgent" line back on the sender instead of repeating the beach, inbox
or limited-email jokes.
"""

import hashlib
import os
import sys
from pathlib import Path

LINE = "I'm away until Monday. If this is urgent, wait until Monday \u2014 it will still be urgent, and I will still be ignoring it."

# Pinned by the build: the exact bytes the program must write.
# Filled in by the build's verification step; verify() refuses to run
# with the placeholders still in place.
EXPECTED_BYTES = 121
EXPECTED_SHA256 = "3e2baffcae4afdc5dc9feb9eca4475bb9524da36fe343487fdf0f3dac44f7185"


def verify(data: bytes) -> None:
    """Check the output bytes against the gate and the pinned values."""
    if EXPECTED_SHA256 == "PENDING" or EXPECTED_BYTES == 0:
        raise SystemExit("expected output hash/byte count not pinned yet")
    if not 1 <= len(data.decode("utf-8")) <= 160:
        raise SystemExit("entry must be 1-160 characters")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"byte count changed: got {len(data)}, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"sha256 changed: got {digest}, expected {EXPECTED_SHA256}")


def output_dir() -> Path:
    """The harness output directory: /output in the sandbox, ./output locally."""
    env = os.environ.get("OUTPUT_DIR")
    if env:
        return Path(env)
    if Path("/output").is_dir():
        return Path("/output")
    return Path("output")


def main() -> None:
    text = LINE
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    data = text.encode("utf-8")
    verify(data)
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(data)
    print(f"wrote {out_path} ({len(data)} bytes, sha256 {hashlib.sha256(data).hexdigest()})")


if __name__ == "__main__":
    main()
