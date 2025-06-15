# main.py
import os
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP # The McpEndpoint is part of the FastApiMCP instance
from pydantic import BaseModel, Field
import uvicorn
import google.generativeai as genai # Import the Google Generative AI library

# --- Configuration ---
# BEST PRACTICE: Load your API key from a Codespaces secret.
# The secret should be named API_KEY_GEMINI_1.
api_key = os.environ.get("API_KEY_GEMINI_1")
if api_key:
    genai.configure(api_key=api_key)

app = FastAPI(title="MCP-Enabled LLM Service")

# The MCP instance must be created before its decorator can be used.
mcp = FastApiMCP(app, name="My Custom Google LLM Service")

# --- Define the data models for your MCP endpoint (these don't need to change) ---
class ChatRequest(BaseModel):
    """The data we expect to receive in the request."""
    prompt: str = Field(..., description="The user's prompt for the LLM.")

class ChatResponse(BaseModel):
    """The data we will send back."""
    content: str = Field(..., description="The LLM's generated response.")


# --- Create the MCP Endpoint ---
# The endpoint decorator comes from the mcp instance itself.
@mcp.endpoint(
    id="generate_text",
    title="Generate Text with LLM",
    description="Sends a prompt to an LLM and gets a response.",
    request_schema=ChatRequest,
    response_schema=ChatResponse,
)
async def generate_text(request: ChatRequest) -> ChatResponse:
    """
    This function is the core of your service.
    1. It receives an MCP request.
    2. It calls the Google Generative AI API.
    3. It returns an MCP response.
    """
    print(f"Received prompt: {request.prompt}")
    
    # Initialize the Generative Model
    # You can choose other models like 'gemini-1.5-pro-latest'
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # Call the actual LLM
    response = model.generate_content(request.prompt)
    
    # Extract the response content
    response_content = response.text
    print(f"LLM Response: {response_content}")
    
    # Return the response in the format defined by ChatResponse
    return ChatResponse(content=response_content)


# --- Mount the MCP Server ---
# The decorator now handles registration, so we only need to mount.
mcp.mount()

# --- Run the application ---
if __name__ == "__main__":
    if not api_key:
        print("ERROR: API_KEY_GEMINI_1 environment variable not set.")
    else:
        uvicorn.run(app, host="0.0.0.0", port=8000)
