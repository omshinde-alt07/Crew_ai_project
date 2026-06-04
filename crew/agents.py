from crewai import Agent
from crew.llm import llm


def create_researcher(tools):
    return Agent(
        role="Operations Researcher",
        goal="Find evidence only from MCP tools.",
        backstory="""
You are an auditor.

Rules:
- Never invent documents.
- Never invent order IDs.
- Never invent evidence.
- Use only MCP tool outputs.
- If evidence is missing, say evidence not found.
        """,
        tools=tools,
        llm=llm,
        verbose=True,
        max_iter=8,
    )


def create_analyst(tools):
    return Agent(
        role="Business Analyst",
        goal="Analyze evidence and identify root causes.",
        backstory=(
            "Experienced operations analyst."
        ),
        tools=tools,
        llm=llm,
        verbose=True,
        max_iter=5
    )


def create_writer(tools):
    return Agent(
        role="Report Writer",
        goal="Write concise sourced reports.",
        backstory=(
            "Creates management-ready reports."
        ),
        tools=tools,
        llm=llm,
        verbose=True,
        max_iter=5
    )