from .scraper_tool import execute_scraper
from .mysql_tool import execute_mysql_query
from .weather_tool import execute_weather
from .search_tool import execute_search
from .calc_tool import execute_calculator
from .finance_tool import execute_finance

TOOL_MAP = {
    "web_scraper": execute_scraper,
    "mysql_database": execute_mysql_query,
    "weather_api": execute_weather,
    "web_search": execute_search,
    "calculator": execute_calculator,
    "finance_api": execute_finance,
}