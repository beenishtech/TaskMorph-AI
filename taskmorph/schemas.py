from typing import TypedDict, List, Literal
from pydantic import BaseModel


# Structured output formats expected from Gemini
class TaskList(BaseModel):
    tasks: List[str]


class PrioritizedTask(BaseModel):
    task: str
    priority: Literal["High", "Medium", "Low"]


class PrioritizedList(BaseModel):
    items: List[PrioritizedTask]


# LangGraph shared state (every node reads and updates this)
class State(TypedDict):
    user_input: str
    tasks: List[str]
    prioritized: List[dict]
    output: str