from datetime import date
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from taskmorph.schemas import State, TaskList, PrioritizedList

load_dotenv()  # loads GOOGLE_API_KEY from .env

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


# Node 1: Task extraction
def extract_tasks(state: State):
    extractor = llm.with_structured_output(TaskList)
    result = extractor.invoke(
        "Extract every individual task from this message. "
        "Write each task in clear, short English, even if the message is in "
        "Roman Urdu or another language. "
        "Keep deadlines (like 'tomorrow') inside the task text.\n\n"
        f"{state['user_input']}"
    )
    return {"tasks": result.tasks}


# Node 2: Prioritization
def prioritize(state: State):
    ranker = llm.with_structured_output(PrioritizedList)
    result = ranker.invoke(
        f"Today is {date.today()}. Assign High, Medium or Low priority to each "
        "task based on urgency and deadline. Keep the task text in English "
        "exactly as given.\n\nTasks:\n"
        + "\n".join(state["tasks"])
    )
    return {"prioritized": [i.model_dump() for i in result.items]}


# Node 3: Format results (emojis kept)
def format_results(state: State):
    icons = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
    order = {"High": 0, "Medium": 1, "Low": 2}
    items = sorted(state["prioritized"], key=lambda x: order[x["priority"]])

    lines = ["📋 Your To-Do List", ""]
    for i in items:
        lines.append(f"{icons[i['priority']]} {i['priority']:<7} {i['task']}")
    return {"output": "\n".join(lines)}