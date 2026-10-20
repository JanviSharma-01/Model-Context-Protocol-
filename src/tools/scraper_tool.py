import requests
from bs4 import BeautifulSoup

def execute_scraper(url: str) -> str:
    """Scrapes paragraph content from a target URL."""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return " ".join(paragraphs[:3]) if paragraphs else "No readable paragraph text found."
    except Exception as e:
        return f"Scraper notice: Executed with fallback response for '{url}'."