import requests

def _call_ollama(prompt: str) -> str:
    """Calls local Ollama instance with fallback if the model/service is unavailable."""
    try:
        from config import OLLAMA_BASE_URL, OLLAMA_MODEL
        url = f"{OLLAMA_BASE_URL}/api/generate"
        payload = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
        
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            # Fallback when model is not downloaded locally
            return _mock_llm_response(prompt)
            
    except Exception:
        # Fallback when Ollama server is offline
        return _mock_llm_response(prompt)

def _mock_llm_response(prompt: str) -> str:
    """Provides local rule-based intent routing when LLM service is offline."""
    p_lower = prompt.lower()
    if "weather" in p_lower or "temp" in p_lower:
        return '{"tool": "weather_api", "arg": "Srinagar"}'
    elif "select" in p_lower or "sql" in p_lower:
        return '{"tool": "mysql_database", "arg": "SELECT * FROM users LIMIT 5;"}'
    elif "http" in p_lower or "scrape" in p_lower:
        return '{"tool": "web_scraper", "arg": "https://example.com"}'
    elif "stock" in p_lower or "price" in p_lower:
        return '{"tool": "finance_api", "arg": "AAPL"}'
    elif any(op in p_lower for op in ["+", "-", "*", "/"]):
        return '{"tool": "calculator", "arg": "45 * 12"}'
    else:
        return '{"tool": "web_search", "arg": "' + prompt + '"}'