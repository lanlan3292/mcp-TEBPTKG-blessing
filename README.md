# mcp-TEBPTKG-blessing

一个简单的 MCP Server，用于从 `The Error Blessing Pack That Keeps Giving.txt` 中随机抽取一条祝福语。

## 行为

- 忽略第 1–9 行。
- 从第 10 行一直读取到文件末尾。
- 空行不参与随机抽取。
- 每次调用 `random_blessing` 时重新读取文件并随机选择一条，因此修改源文件后无需重启服务。

## 安装

```bash
pip install -e .
```

将 `The Error Blessing Pack That Keeps Giving.txt` 放在 `server.py` 同目录。

也可以通过环境变量指定文件路径：

```bash
BLESSING_FILE=/path/to/The\ Error\ Blessing\ Pack\ That\ Keeps\ Giving.txt python server.py
```

## 运行

```bash
python server.py
```

MCP 工具名：`random_blessing`

## MCP 客户端配置示例

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

> 数据文件未随本仓库提交；请自行将原始 `The Error Blessing Pack That Keeps Giving.txt` 放到运行目录，或设置 `BLESSING_FILE`。
