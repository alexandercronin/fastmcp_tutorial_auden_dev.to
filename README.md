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
- Press that the setting button and then ensure that you MCP server selected and the endpoints are ticked
- Ensure that there is no files open as they will get priority in the execution of the context of the server
- Enter the text "say hello"
- The agent will reply saying "Ran `say_hello` - fastapi-mcp (MCP Server) Hello My Friend"

# Troubleshooting

1. Open the command console (Ctrl+p)
2. Press `>` and type `MCP` select the server listed, this is referenced from the `mcp.json` file in `.vscode` settings folder
3. Select `List Servers`
4. Select the server you want
5. Select `Restart Server`
6. Repeat the steps and this time select show output. You should see something like the output below:

```
2025-06-15 02:45:01.544 [info] Starting server fastapi-mcp
2025-06-15 02:45:01.545 [info] Connection state: Starting
2025-06-15 02:45:01.563 [info] Starting server from LocalProcess extension host
2025-06-15 02:45:01.580 [info] Connection state: Starting
2025-06-15 02:45:01.581 [info] Connection state: Running
2025-06-15 02:45:01.818 [warning] [server stderr] [84919] Using specified callback port: 8080
2025-06-15 02:45:01.819 [warning] [server stderr] [84919] [84919] Connecting to remote server: http://localhost:8000/mcp
2025-06-15 02:45:01.819 [warning] [server stderr] [84919] Using transport strategy: http-first
2025-06-15 02:45:01.855 [warning] [server stderr] [84919] Received error: Error POSTing to endpoint (HTTP 405): {"detail":"Method Not Allowed"}
2025-06-15 02:45:01.855 [warning] [server stderr] [84919] Recursively reconnecting for reason: falling-back-to-alternate-transport
2025-06-15 02:45:01.855 [warning] [server stderr] [84919] [84919] Connecting to remote server: http://localhost:8000/mcp
2025-06-15 02:45:01.855 [warning] [server stderr] [84919] Using transport strategy: sse-only
2025-06-15 02:45:01.859 [warning] [server stderr] [84919] Connected to remote server using SSEClientTransport
2025-06-15 02:45:01.859 [warning] [server stderr] [84919] Local STDIO server running
2025-06-15 02:45:01.859 [warning] [server stderr] [84919] Proxy established successfully between local STDIO and remote SSEClientTransport
2025-06-15 02:45:01.859 [warning] [server stderr] [84919] Press Ctrl+C to exit
2025-06-15 02:45:01.860 [warning] [server stderr] [84919] [Local→Remote] initialize
2025-06-15 02:45:01.860 [warning] [server stderr] [84919] {
2025-06-15 02:45:01.860 [warning] [server stderr]   "jsonrpc": "2.0",
2025-06-15 02:45:01.860 [warning] [server stderr]   "id": 1,
2025-06-15 02:45:01.860 [warning] [server stderr]   "method": "initialize",
2025-06-15 02:45:01.860 [warning] [server stderr]   "params": {
2025-06-15 02:45:01.860 [warning] [server stderr]     "protocolVersion": "2025-03-26",
2025-06-15 02:45:01.861 [warning] [server stderr]     "capabilities": {
2025-06-15 02:45:01.861 [warning] [server stderr]       "roots": {
2025-06-15 02:45:01.861 [warning] [server stderr]         "listChanged": true
2025-06-15 02:45:01.861 [warning] [server stderr]       },
2025-06-15 02:45:01.861 [warning] [server stderr]       "sampling": {}
2025-06-15 02:45:01.861 [warning] [server stderr]     },
2025-06-15 02:45:01.861 [warning] [server stderr]     "clientInfo": {
2025-06-15 02:45:01.861 [warning] [server stderr]       "name": "Visual Studio Code (via mcp-remote 0.1.15)",
2025-06-15 02:45:01.861 [warning] [server stderr]       "version": "1.101.0"
2025-06-15 02:45:01.861 [warning] [server stderr]     }
2025-06-15 02:45:01.861 [warning] [server stderr]   }
2025-06-15 02:45:01.861 [warning] [server stderr] }
2025-06-15 02:45:01.865 [warning] [server stderr] [84919] [Remote→Local] 1
2025-06-15 02:45:01.866 [warning] [server stderr] [84919] [Local→Remote] notifications/initialized
2025-06-15 02:45:01.866 [warning] [server stderr] [84919] [Local→Remote] tools/list
2025-06-15 02:45:01.870 [warning] [server stderr] [84919] [Remote→Local] 2
2025-06-15 02:45:01.870 [info] Discovered 2 tools
```

- If you are offered a command like `python main.py curl http://localhost:8000/hello` then it means that it may be reading this context from an open main.py file, or the server is not running. 
- if when prompted to use the tool/agent you are getting messages to say the agent was cancelled then select continue for the session and it should perform better. 

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
