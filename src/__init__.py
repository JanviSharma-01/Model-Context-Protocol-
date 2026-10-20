from .calc_tool import run_calculator
from .finance_tool import fetch_finance_data
from .mysql_tool import execute_mysql_query
from .scraper_tool import scrape_web_page
from .search_tool import search_web
from .weather_tool import get_weather

TOOL_MAP = {
    "calculator": run_calculator,
    "finance_api": fetch_finance_data,
    "mysql_database": execute_mysql_query,
    "web_scraper": scrape_web_page,
    "web_search": search_web,
    "weather_api": get_weather,
}
