from crewai import LLM

llm = LLM(
    model="ollama/llama3.2:latest",
    base_url="http://localhost:11434"
)

response = llm.call("Say hello in one sentence.")

print(response)