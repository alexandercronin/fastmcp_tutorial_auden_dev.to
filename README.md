## fastmcp_tutorial_auden_dev.to

Based on tutorial implementation of https://dev.to/auden/introducing-fastapi-mcp-effortless-ai-integration-for-your-fastapi-apis-2c8c

Implementation is currently incomplete as attemting to enable 
- [ ] Access to multiple LLMs
- [ ] Calls from CLI + multiple agent 

# Installation

install

```sh
./install.sh
```

run

```sh
./run.sh
```

# Usage on VSCode

- Open copilot chat
- Ensure the `Agent` item is selected from the drop down
- Enter the text "Run the /hello endpoint"
- Safety feature of copilot will ask you if you wish to execute a command like `curl http://localhost:8000/hello`
- Expected reply : {"message":"Hello World"}

# Troubleshooting

1. Ensure the fastapi application is work
2. Ensure that the MCP server us running
3. Ensure that the MCP debug server output is something like :

```bash
2025-06-15 00:53:50.688 [info] Connection state: Error Process exited with code 143
2025-06-15 00:53:56.669 [info] Starting server fastapi-mcp
2025-06-15 00:53:56.670 [info] Connection state: Starting
2025-06-15 00:53:56.695 [info] Starting server from Remote extension host
2025-06-15 00:53:56.746 [info] Connection state: Starting
2025-06-15 00:53:56.746 [info] Connection state: Running
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] Using specified callback port: 8080
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] [95610] Connecting to remote server: http://localhost:8000/mcp
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] Using transport strategy: http-first
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] Received error: Error POSTing to endpoint (HTTP 405): {"detail":"Method Not Allowed"}
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] Recursively reconnecting for reason: falling-back-to-alternate-transport
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] [95610] Connecting to remote server: http://localhost:8000/mcp
2025-06-15 00:53:57.589 [warning] [server stderr] [95610] Using transport strategy: sse-only
2025-06-15 00:53:57.591 [warning] [server stderr] [95610] Connected to remote server using SSEClientTransport
2025-06-15 00:53:57.591 [warning] [server stderr] [95610] Local STDIO server running
2025-06-15 00:53:57.592 [warning] [server stderr] [95610] Proxy established successfully between local STDIO and remote SSEClientTransport
2025-06-15 00:53:57.592 [warning] [server stderr] [95610] Press Ctrl+C to exit
2025-06-15 00:53:57.592 [warning] [server stderr] [95610] [Local→Remote] initialize
2025-06-15 00:53:57.592 [warning] [server stderr] [95610] {
2025-06-15 00:53:57.592 [warning] [server stderr]   "jsonrpc": "2.0",
2025-06-15 00:53:57.592 [warning] [server stderr]   "id": 1,
2025-06-15 00:53:57.592 [warning] [server stderr]   "method": "initialize",
2025-06-15 00:53:57.592 [warning] [server stderr]   "params": {
2025-06-15 00:53:57.592 [warning] [server stderr]     "protocolVersion": "2025-03-26",
2025-06-15 00:53:57.592 [warning] [server stderr]     "capabilities": {
2025-06-15 00:53:57.592 [warning] [server stderr]       "roots": {
2025-06-15 00:53:57.592 [warning] [server stderr]         "listChanged": true
2025-06-15 00:53:57.592 [warning] [server stderr]       },
2025-06-15 00:53:57.592 [warning] [server stderr]       "sampling": {}
2025-06-15 00:53:57.592 [warning] [server stderr]     },
2025-06-15 00:53:57.592 [warning] [server stderr]     "clientInfo": {
2025-06-15 00:53:57.592 [warning] [server stderr]       "name": "Visual Studio Code (via mcp-remote 0.1.15)",
2025-06-15 00:53:57.592 [warning] [server stderr]       "version": "1.101.0"
2025-06-15 00:53:57.592 [warning] [server stderr]     }
2025-06-15 00:53:57.592 [warning] [server stderr]   }
2025-06-15 00:53:57.592 [warning] [server stderr] }
2025-06-15 00:53:57.593 [warning] [server stderr] [95610] [Remote→Local] 1
2025-06-15 00:53:57.633 [warning] [server stderr] [95610] [Local→Remote] notifications/initialized
2025-06-15 00:53:57.634 [warning] [server stderr] [95610] [Local→Remote] tools/list
2025-06-15 00:53:57.665 [warning] [server stderr] [95610] [Remote→Local] 2
2025-06-15 00:53:57.665 [info] Discovered 1 tools
```
- If you are offered a command like `python main.py curl http://localhost:8000/hello` then it means that the MCP server has not detected the uvicorn server and because the installation is running from a venv the launch will fail.

# Resources

## FastMCP

- https://github.com/jlowin/fastmcp
- https://gofastmcp.com/getting-started/installation

## MCP

- https://github.com/modelcontextprotocol
- https://modelcontextprotocol.io/introduction

# MCP on VSCode

https://code.visualstudio.com/docs/copilot/chat/mcp-servers
https://code.visualstudio.com/blogs/2025/06/12/full-mcp-spec-support
https://www.youtube.com/shorts/vhdRUJlgwD4

# Links

MCP general video tutorial;

- https://www.youtube.com/watch?v=rnljvmHorQw
- https://medium.com/towards-agi/how-to-set-up-and-use-vscode-mcp-server-352c1e6f42e9

# Githuhb MCP

- https://docs.github.com/en/copilot/customizing-copilot/using-model-context-protocol/using-the-github-mcp-server
