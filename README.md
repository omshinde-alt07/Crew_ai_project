# MCP + CrewAI Supply Chain Investigation System

## Overview

This project demonstrates how CrewAI agents can interact with an MCP (Model Context Protocol) server to investigate delayed orders using enterprise documents and structured business data.

The system uses:

* CrewAI Multi-Agent Framework
* MCP Server
* Ollama (Llama 3.2)
* Local Knowledge Base
* CSV Order Data
* Automated Report Generation

The agents investigate delayed orders, identify causes, collect supporting evidence, and generate a final report.

---

# Business Problem

A supply chain team wants to understand:

* Which orders are delayed?
* Which products are affected?
* What evidence supports the delays?
* What operational actions should be taken?

Instead of manually reviewing documents, agents automatically analyze company records and generate an investigation report.

- [Project Demo Video](https://notebooklm.google.com/notebook/28cc4f5d-8c99-47ab-aa9a-71f5b6da6cb1/artifact/025c2572-8b6b-4c1d-8403-d696997a9011?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_2&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_2_)

- [Project Presentation (PPT)](https://notebooklm.google.com/notebook/28cc4f5d-8c99-47ab-aa9a-71f5b6da6cb1/artifact/ee89703d-fc27-4cd7-b070-d5c7c22a60a3?utm_source=nlm_web_share&utm_medium=google_oo&utm_campaign=art_share_2&utm_content=&utm_smc=nlm_web_share_google_oo_art_share_2_)

---

# Architecture

```text
                    +----------------+
                    |    User Query  |
                    +--------+-------+
                             |
                             v
                    +----------------+
                    |   CrewAI Crew  |
                    +--------+-------+
                             |
         -----------------------------------------
         |                   |                   |
         v                   v                   v

+----------------+  +----------------+  +----------------+
| Research Agent |  | Analyst Agent  |  | Writer Agent   |
+--------+-------+  +--------+-------+  +--------+-------+
         |                   |                   |
         -----------------------------------------
                             |
                             v
                    +----------------+
                    |   MCP Server    |
                    +--------+-------+
                             |
          ---------------------------------------
          |                 |                   |
          v                 v                   v

   orders.csv      Business Documents      Reports
                                       (Markdown Output)

```

---

# Agent Workflow

## Agent 1: Operations Researcher

Responsibilities:

* Call MCP tools
* Retrieve delayed orders
* Retrieve supporting evidence
* Identify affected products

Tools Used:

* investigate_delayed_orders()
* get_delayed_orders()
* read_record()

Output:

* Grounded evidence report

---

## Agent 2: Business Analyst

Responsibilities:

* Analyze evidence
* Determine causes
* Identify business impact
* Summarize findings

Output:

* Structured operational analysis

---

## Agent 3: Report Writer

Responsibilities:

* Create final report
* Save report using MCP tool
* Produce management-ready output

Tools Used:

* save_report()

Output:

* Markdown report

---

# MCP Tools

## search_documents(query)

Searches company documents.

Example:

```python
search_documents("Laptop")
```

---

## read_record(id)

Reads:

* Document contents
* Order information

Example:

```python
read_record("product_laptop.txt")
```

---

## get_delayed_orders()

Returns delayed orders.

Example:

```python
[
    {
        "order_id":1001,
        "product":"Laptop",
        "status":"Delayed"
    }
]
```

---

## get_document_list()

Returns available documents.

---

## investigate_delayed_orders()

Returns:

* Delayed orders
* Evidence documents

Used by Research Agent.

---

## save_report()

Stores final report.

Output:

```json
{
  "status":"saved",
  "file":"outputs/reports/report.md"
}
```

---

# Dataset

## Documents

```text
inventory_policy.txt
shipping_policy.txt
returns_policy.txt
vendor_agreement.txt
product_laptop.txt
product_mouse.txt
support_ticket_001.txt
support_ticket_002.txt
support_ticket_003.txt
warehouse_guidelines.txt
```

## Orders

```csv
order_id,product,quantity,status
1001,Laptop,5,Delayed
1002,Mouse,10,Delivered
...
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Start Ollama

```bash
ollama serve
```

Verify:

```bash
ollama list
```

Expected:

```text
llama3.2
```

---

# Run Application

```bash
python main.py
```

---

# Example Query

```text
Which delayed orders are impacted by stock shortages and what evidence supports this conclusion?
```

---

# Example Output

```text
Affected Orders:
1001
1003
1005
1008
1010

Affected Product:
Laptop

Evidence:
product_laptop.txt
inventory_policy.txt
support_ticket_001.txt
support_ticket_003.txt
vendor_agreement.txt
```

---

# High Level Design (HLD)

## Presentation Layer

* User Query
* CLI Interface

## Orchestration Layer

* CrewAI
* Agents
* Tasks

## Integration Layer

* MCP Server
* Tool Registry

## Data Layer

* orders.csv
* policy documents
* support tickets

## Output Layer

* Markdown Reports
* Saved Investigations

---

# Test Cases

## Test Case 1

### Input

```text
Which delayed orders are impacted by stock shortages?
```

### Expected Result

```text
Orders:
1001
1003
1005
1008
1010

Product:
Laptop
```

Status: PASS

---

## Test Case 2

### Input

```python
get_delayed_orders()
```

### Expected Result

Returns 5 delayed laptop orders.

Status: PASS

---

## Test Case 3

### Input

```python
read_record("product_laptop.txt")
```

### Expected Result

Contains:

```text
Frequent stock shortages
```

Status: PASS

---

## Test Case 4

### Input

```python
save_report(...)
```

### Expected Result

```json
{
  "status":"saved"
}
```

Status: PASS

---

# Future Enhancements

* Vector Database Integration
* RAG Pipeline
* Multi-tenant MCP Server
* Streamlit Dashboard
* Real-Time Inventory APIs
* Supplier Risk Prediction
* Autonomous Supply Chain Agents

---

# Technology Stack

* Python 3.11
* CrewAI
* MCP SDK
* Ollama
* Llama 3.2
* Pandas
* Markdown Reporting

---

# Author

Om Shinde
