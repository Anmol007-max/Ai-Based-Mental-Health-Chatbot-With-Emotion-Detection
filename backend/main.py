# Step1: Setup FastAPI backend
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from backend.ai_agent import graph, SYSTEM_PROMPT, parse_response

app = FastAPI()

# Step2: Receive and validate request from Frontend
class Query(BaseModel):
    message: str



@app.post("/ask")
async def ask(query: Query):
    try:
        print(f"Received query: {query.message}")
        inputs = {"messages": [("system", SYSTEM_PROMPT), ("user", query.message)]}
        print("Streaming graph...")
        stream = graph.stream(inputs, stream_mode="updates")
        print("Parsing response...")
        tool_called_name, final_response = parse_response(stream)
        print(f"Tool: {tool_called_name}, Response: {final_response[:100] if final_response else 'None'}...")
        
        # Step3: Send response to the frontend
        return {
            "response": final_response or "I apologize, but I couldn't generate a response. Please try again.",
            "tool_called": tool_called_name
        }
    except Exception as e:
        print(f"ERROR in /ask endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            "response": f"Error: {str(e)}",
            "tool_called": "error"
        }


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)






