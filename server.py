"""MCP server for randomly drawing a blessing from a text file.

The source file is read at runtime. Lines 1-9 are ignored; line 10 through
EOF form the random pool. Blank lines are ignored.
"""

from __future__ import annotations

import os
import random
from pathlib import Path

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("TEBPTKG Blessing")

DEFAULT_SOURCE = "The Error Blessing Pack That Keeps Giving.txt"


def _source_path() -> Path:
    return Path(os.environ.get("BLESSING_FILE", DEFAULT_SOURCE))


def _load_blessings() -> list[str]:
    path = _source_path()
    if not path.is_file():
        raise FileNotFoundError(
            f"Blessing source file not found: {path}. "
            "Put the text file beside server.py or set BLESSING_FILE."
        )

    # splitlines() gives us logical lines without retaining line endings.
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    # Human-readable line numbers are 1-based: index 9 is line 10.
    return [line for line in lines[9:] if line.strip()]


@mcp.tool()
def random_blessing() -> str:
    """Randomly return one non-empty line from source line 10 through EOF."""
    blessings = _load_blessings()
    if not blessings:
        raise ValueError("No non-empty blessing lines found from line 10 onward.")
    return random.choice(blessings)


if __name__ == "__main__":
    mcp.run()
