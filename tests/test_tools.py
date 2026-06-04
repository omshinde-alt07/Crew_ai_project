import os
import sys

print("Current directory:", os.getcwd())
print("Python path:", sys.path[:3])

sys.path.append(os.path.abspath("."))

from server.mcp_server import search_documents, read_record

print(search_documents("Laptop"))
print(read_record("product_laptop.txt"))
print(read_record("1001"))