from langchain_community.tools import DuckDuckGoSearchRun

def search_web(query: str) -> str:
    """Search the web using DuckDuckGo and return the results."""
    try:
        print("Searching web...")
        search_tool = DuckDuckGoSearchRun()
        results = search_tool.run(query)
        return results
    except Exception as error:
        print("Error during web search:", error)
        return "An error occurred while searching the web."