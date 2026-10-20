from typing import TypedDict, List, Literal
from pydantic import BaseModel


# Gemini se jo structured output chahiye
class TaskList(BaseModel):
    tasks: List[str]


class PrioritizedTask(BaseModel):
    task: str
    priority: Literal["High", "Medium", "Low"]


class PrioritizedList(BaseModel):
    items: List[PrioritizedTask]


# LangGraph ki shared state (har node isse padhta/update karta hai)
class State(TypedDict):
    user_input: str
    tasks: List[str]
    prioritized: List[dict]
    output: str