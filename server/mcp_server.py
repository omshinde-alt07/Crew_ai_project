from pathlib import Path
from datetime import datetime
import pandas as pd

from mcp.server.fastmcp import FastMCP

# --------------------------------------------------
# Configuration
# --------------------------------------------------

DOCS_DIR = Path("data/docs")
CSV_FILE = Path("data/orders.csv")
REPORT_DIR = Path("outputs/reports")

REPORT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# MCP Server
# --------------------------------------------------

mcp = FastMCP("OperationsAssistant")

# --------------------------------------------------
# Tool 1
# Search documents
# --------------------------------------------------

@mcp.tool()
def search_documents(query: str):
    query = str(query).lower()

    results = []

    for file in DOCS_DIR.glob("*.txt"):
        content = file.read_text(encoding="utf-8")

        if query in content.lower():
            results.append({
                "document": file.name,
                "preview": content[:300]
            })

    return results


# --------------------------------------------------
# Tool 2
# Read document or order record
# --------------------------------------------------

@mcp.tool()
def read_record(record_id: str) -> dict:
    """
    Read a document or order.
    """

    # document lookup

    doc_file = DOCS_DIR / record_id

    if doc_file.exists():

        return {
            "type": "document",
            "name": doc_file.name,
            "content": doc_file.read_text(
                encoding="utf-8"
            )
        }

    # order lookup

    try:

        df = pd.read_csv(CSV_FILE)

        order_id = int(record_id)

        row = df[
            df["order_id"] == order_id
        ]

        if not row.empty:

            return {
                "type": "order",
                "data": row.iloc[0].to_dict()
            }

    except Exception:
        pass

    return {
        "error": f"{record_id} not found"
    }


# --------------------------------------------------
# Tool 3
# Save report
# --------------------------------------------------

@mcp.tool()
def save_report(
    title: str,
    content: str
) -> dict:
    """
    Save markdown report.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        REPORT_DIR
        / f"{timestamp}_{title.replace(' ','_')}.md"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return {
        "status": "saved",
        "file": str(filename)
    }


@mcp.tool()
def get_delayed_orders():
    """
    Return all delayed orders.
    """

    df = pd.read_csv(CSV_FILE)

    delayed = df[
        df["status"] == "Delayed"
    ]

    return delayed.to_dict(
        orient="records"
    )

@mcp.tool()
def get_document_list():
    return [f.name for f in DOCS_DIR.glob("*.txt")]

@mcp.tool()
def investigate_delayed_orders():
    """
    Return delayed orders with supporting evidence.
    """

    df = pd.read_csv(CSV_FILE)

    delayed = df[df["status"] == "Delayed"]

    evidence = []

    for file in DOCS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        if any(
            keyword in text.lower()
            for keyword in [
                "laptop",
                "stock",
                "delay",
                "replenishment"
            ]
        ):
            evidence.append({
                "document": file.name,
                "content": text
            })

    return {
        "orders": delayed.to_dict(
            orient="records"
        ),
        "evidence": evidence
    }

# --------------------------------------------------
# Run server
# --------------------------------------------------

if __name__ == "__main__":
    mcp.run()