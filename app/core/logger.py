import logging

logger = logging.getLogger("interactive_agent")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


### app/tools/custom_tools.py
from langchain.tools import Tool

def duckduckgo_search(query: str) -> str:
    # Dummy implementation
    return f"DuckDuckGo results for '{query}'"

tools = [
    Tool(
        name="duckduckgo_search_results",
        func=duckduckgo_search,
        description="Search DuckDuckGo for real-time info"
    ),
]

