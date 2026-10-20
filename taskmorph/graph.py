from langgraph.graph import StateGraph, START, END

from taskmorph.schemas import State
from taskmorph.nodes import extract_tasks, prioritize, format_results


def build_graph():
    g = StateGraph(State)
    g.add_node("extract", extract_tasks)
    g.add_node("prioritize", prioritize)
    g.add_node("format", format_results)

    g.add_edge(START, "extract")
    g.add_edge("extract", "prioritize")
    g.add_edge("prioritize", "format")
    g.add_edge("format", END)
    return g.compile()