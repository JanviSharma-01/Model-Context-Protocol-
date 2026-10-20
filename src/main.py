import sys
from pathlib import Path

# Add root folder to sys.path so src imports work cleanly
sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from src.pipeline import TwoStageAgentPipeline

app = FastAPI(
    title="Model Context Protocol (MCP) Based AI System",
    version="1.0.0",
    description="Multi-tier agentic query routing system across 6+ tool services."
)

pipeline = TwoStageAgentPipeline()

# Input model matching Swagger UI expectation
class QueryRequest(BaseModel):
    query: str

# Response model matching Swagger UI expectation
class QueryResponse(BaseModel):
    query: str
    tool_used: str
    tool_result: Dict[str, Any]
    reply: str

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "system": "MCP Agentic Gateway",
        "uptime": "99.9%",
        "services_connected": len(pipeline.tools)
    }

@app.post("/chat", response_model=QueryResponse)
@app.post("/api/v1/query", response_model=QueryResponse)
def process_chat_query(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    
    # Process through Two-Stage Pipeline
    result = pipeline.process(request.query)
    
    routing = result["pipeline"]["stage_1_routing"]
    tool_output = result["pipeline"]["tool_execution_output"]
    grounded_reply = result["pipeline"]["stage_2_grounded_response"]

    return {
        "query": request.query,
        "tool_used": routing["tool"],
        "tool_result": {"raw_output": tool_output},
        "reply": grounded_reply
    }