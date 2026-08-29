#!/usr/bin/env python3
"""MCP server for the TEBPTKG static blessing pack."""

from __future__ import annotations

import random
from pathlib import Path

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("mcp-TEBPTKG-blessing")
SOURCE_FILE = (
    Path(__file__).parent
    / "The_Error_Blessing_Pack_That_Keeps_Giving"
    / "The Error Blessing Pack That Keeps Giving.txt"
)


def load_blessings() -> list[str]:
    """Load the static blessing pool from line 10 through EOF."""
    if not SOURCE_FILE.is_file():
        raise FileNotFoundError(
            f"Bundled blessing file not found: {SOURCE_FILE.name}"
        )

    lines = SOURCE_FILE.read_text(encoding="utf-8-sig").splitlines()
    return [line for line in lines[9:] if line.strip()]


@mcp.tool()
def random_blessing() -> str:
    """Return one random non-empty blessing from line 10 through the end."""
    blessings = load_blessings()
    if not blessings:
        raise ValueError("The static blessing pack contains no usable entries.")
    return random.choice(blessings)


if __name__ == "__main__":
    mcp.run()
