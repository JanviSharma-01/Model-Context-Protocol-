# Model Context Protocol (MCP) Based AI Agent Gateway

A production-grade, multi-tier agentic system engineered with a **Two-Stage LLM Inference Pipeline** that dynamically routes user prompts across 6 distinct tool services, executes context retrieval, and synthesizes grounded final responses.

---

## 🌟 Key Features

* **Two-Stage Inference Architecture:**
  * **Stage 1 (Intent Classification & Dynamic Routing):** Evaluates user queries and routes them to appropriate micro-tool services.
  * **Stage 2 (Grounded Response Synthesis):** Integrates raw tool outputs with user prompts to generate factual, context-aware responses.
* **6 Micro-Tool Services:**
  1. **Weather API (`weather_tool.py`):** Live/mock weather contextual data retrieval.
  2. **MySQL Execution (`mysql_tool.py`):** Relational database query interface via PyMySQL.
  3. **Web Scraper (`scraper_tool.py`):** Web page content extraction using BeautifulSoup4.
  4. **Financial Markets (`finance_tool.py`):** Market ticker and equity data fetcher.
  5. **Calculator (`calc_tool.py`):** Safe mathematical expression evaluator.
  6. **Web Search (`search_tool.py`):** Fallback information retrieval engine.
* **Resilient LLM Integration:** Local Ollama support with automatic offline rule-based fallback handlers to guarantee high availability (zero 500 crashes).
* **FastAPI Gateway:** Fully interactive OpenAPI / Swagger UI interface for local testing and integration.

---

## 📁 Repository Structure

```text
Model-Context-Protocol/
│
├── config.py                  # Environment variables & service configurations
├── requirements.txt           # Project dependencies
├── README.md                  # System documentation
│
├── src/                       # Application source code
│   ├── __init__.py            # Root package initializer
│   ├── main.py                # FastAPI endpoints & application routing
│   ├── pipeline.py            # Two-Stage Agentic Pipeline logic
│   ├── llm.py                 # LLM caller & offline fallback handlers
│   ├── database.py             # DB Connection handlers
│   └── tools/                 # Micro-tool registry
│       ├── __init__.py        # Tool map registry
│       ├── calc_tool.py       # Calculator module
│       ├── finance_tool.py    # Financial data module
│       ├── mysql_tool.py      # MySQL database interface
│       ├── scraper_tool.py    # Web scraping engine
│       ├── search_tool.py     # Fallback search interface
│       └── weather_tool.py    # Weather information interface
│
└── tests/                     # Automated unit test suite
