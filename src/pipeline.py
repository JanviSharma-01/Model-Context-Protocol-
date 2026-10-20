from src.tools import TOOL_MAP

class TwoStageAgentPipeline:
    def __init__(self):
        self.tools = TOOL_MAP

    def stage_1_intent_routing(self, user_prompt: str) -> dict:
        """Stage 1: Intent classification & dynamic service selection."""
        prompt_lower = user_prompt.lower()
        
        if "http" in prompt_lower or "scrape" in prompt_lower:
            return {"tool": "web_scraper", "arg": user_prompt.split()[-1]}
        elif any(k in prompt_lower for k in ["select", "sql", "database", "table"]):
            return {"tool": "mysql_database", "arg": "SELECT * FROM users LIMIT 5;"}
        elif any(k in prompt_lower for k in ["weather", "temp", "temperature", "rain"]):
            # Extract the city if provided after "in", else default to Delhi
            words = user_prompt.split()
            city = words[-1].strip("?.!") if "in" in prompt_lower else "Delhi"
            return {"tool": "weather_api", "arg": city}
        elif any(k in prompt_lower for k in ["stock", "price", "ticker", "finance"]):
            return {"tool": "finance_api", "arg": "AAPL"}
        elif any(op in prompt_lower for op in ["+", "-", "*", "/"]):
            return {"tool": "calculator", "arg": user_prompt}
        else:
            return {"tool": "web_search", "arg": user_prompt}

    def stage_2_grounded_generation(self, user_prompt: str, tool_name: str, raw_output: str) -> str:
        """Stage 2: Grounds retrieved tool payload into a final response."""
        return (
            f"Grounding Synthesis:\n"
            f"- Query: '{user_prompt}'\n"
            f"- Selected Service: {tool_name}\n"
            f"- Retrieved Context: {raw_output}\n\n"
            f"Final Response: The system successfully executed {tool_name} and retrieved the grounded data above."
        )

    def process(self, user_prompt: str) -> dict:
        routing = self.stage_1_intent_routing(user_prompt)
        tool_name = routing["tool"]
        tool_arg = routing["arg"]

        tool_fn = self.tools.get(tool_name)
        tool_result = tool_fn(tool_arg) if tool_fn else "Tool execution error."

        grounded_response = self.stage_2_grounded_generation(user_prompt, tool_name, tool_result)

        return {
            "status": "success",
            "pipeline": {
                "stage_1_routing": routing,
                "tool_execution_output": tool_result,
                "stage_2_grounded_response": grounded_response
            }
        }