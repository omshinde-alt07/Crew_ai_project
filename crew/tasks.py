from crewai import Task

def research_task(agent, question):
    return Task(
        description="""
Call investigate_delayed_orders.

Return:

1. Delayed order ids
2. Products
3. Evidence documents

Use only returned evidence.
Do not invent document names.
""",
        expected_output="""
Grounded evidence report.
""",
        agent=agent
    )

def analysis_task(agent, context):
    return Task(
        description="""
        Analyze the evidence.

        Determine:
        - delays
        - causes
        - impacted products
        - supporting evidence
        """,
        expected_output="Structured analysis.",
        context=[context],
        agent=agent
    )


def report_task(agent, context):
    return Task(
        description="""
        Write a final report.

        Include:
        - findings
        - evidence
        - recommendations

        Do not invent information.
        """,
        expected_output="Final markdown report.",
        context=[context],
        agent=agent
    )

def save_task(agent, context):
    return Task(
        description="""
Use save_report tool.

Title:
Delayed Orders Investigation

Save the final report.
""",
        context=[context],
        agent=agent
    )