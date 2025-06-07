from langchain.tools import Tool
import requests
from datetime import datetime
from langchain_community.tools import DuckDuckGoSearchResults

def get_weather(location):
    try:
        response = requests.get(f"https://wttr.in/{location}?format=3")
        if response.status_code == 200:
            return response.text
        return f"Could not fetch weather for {location}."
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

weather_tool = Tool(
    name="GetWeather",
    description="Use this to get the current weather in a city. Input should be a city name.",
    func=get_weather
)

def get_current_date(_input=""):
    return datetime.now().strftime("%B %d, %Y")  # e.g., "June 7, 2025"

date_tool = Tool(
    name="GetCurrentDate",
    description="Returns the current date in human-readable format. Input is ignored.",
    func=get_current_date
)

search_tool = Tool(
    name="duckduckgo_search_results",
    description="Search the web using DuckDuckGo. Input should be a plain query string.",
    func=DuckDuckGoSearchResults().run
)

tools = [search_tool, weather_tool, date_tool]