from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import uvicorn
import os

# # This line securely reads the key from the environment.
# # It returns `None` if the key isn't found, preventing crashes.
# api_key = os.environ.get("API_KEY_GEMINI_1")

# if not api_key:
#     print("ERROR: The OPENAI_API_KEY environment variable is not set!")
# else:
#     # Now you can safely use the api_key variable
#     # For example: client = OpenAI(api_key=api_key)
#     print("API key loaded successfully.")

app = FastAPI(title="Simple API")

@app.get("/hello", operation_id="say_hello")
async def hello():
    """A simple greeting endpoint"""
    return {"message": "Hello World"}

# Expose MCP server§
mcp = FastApiMCP(app, name="Simple MCP Service")
mcp.mount()

print("")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)