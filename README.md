# mcp-TEBPTKG-blessing

MCP server for **The Error Blessing Pack That Keeps Giving**.

## Tool

### `random_blessing`

Randomly returns one blessing from the bundled `The Error Blessing Pack That Keeps Giving.txt`.

The random pool is **line 10 through the end of the file**. Lines 1–9 are intentionally ignored. Blank lines are not returned.

## Run

```bash
pip install -e .
python server.py
```

The server uses MCP stdio transport and can be launched by MCP clients that support local stdio servers.

## MCP client configuration

```json
{
  "mcpServers": {
    "tebptkg-blessing": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

## Architecture

The server is intentionally thin:

1. Read the bundled text file.
2. Ignore lines 1–9.
3. Build the pool from line 10 through EOF.
4. Remove blank lines.
5. Return one entry using Python's random selection.
