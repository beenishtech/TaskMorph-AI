# TaskMorph AI

Turns informal task descriptions into an organized, prioritized to-do list
using Gemini and LangGraph.

## Workflow
User input -> Extract tasks -> Prioritize (High/Medium/Low) -> Format -> To-do list

## Setup
1. python -m venv venv && venv\Scripts\activate
2. pip install -r requirements.txt
3. Create .env with GOOGLE_API_KEY=your_key
4. python main.py