# Save this as main.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import uvicorn

app = FastAPI()

# 1. The "Reception Desk" (for the initial handshake)
# The MCP client will connect here FIRST.
@app.post("/mcp")
async def mcp_handshake():
    """
    This is the reception desk. It gives a single, quick JSON response
    telling the client where the real conversation will happen.
    """
    print("MCP client arrived at reception. Giving directions to the stream.")
    
    # This is the one-time instruction (a simple Python dictionary)
    return {
        "protocol_version": "0.1.0",
        "session_id": "my-simple-session-123",
        "transport": {
            "type": "sse",
            # This URL MUST point to your "Meeting Room" endpoint below
            "endpoint": "/stream/my-simple-session-123" 
        },
        "tool_sets": [
            {
                "id": "my_tools",
                "tools": [{"id": "hello_world", "description": "A simple test tool."}]
            }
        ]
    }


# 2. The "Meeting Room" (for the actual chat)
# The MCP client will connect here SECOND, after visiting the reception desk.
@app.get("/stream/{session_id}")
async def mcp_chat_stream(session_id: str):
    """
    This is the meeting room. It's a real-time chat (SSE stream)
    that stays open.
    """
    async def event_generator():
        print(f"MCP client entered the chat room for session: {session_id}")
        # This is where you will handle the real back-and-forth later.
        # For now, we just keep the connection open with pings.
        while True:
            yield "event: ping\ndata: \n\n"
            await asyncio.sleep(15)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


if __name__ == "__main__":
    # Run this file with a command like: uvicorn main:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)