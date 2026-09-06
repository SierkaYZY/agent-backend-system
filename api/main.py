from fastapi import FastAPI
from pydantic import BaseModel

from agent.runner import run_agent_once


app = FastAPI(
    title="Agent Backend System"
)


class AgentRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/agent")
def run_agent(request: AgentRequest):
    answer = run_agent_once(
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }