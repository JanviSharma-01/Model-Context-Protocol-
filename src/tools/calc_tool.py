def execute_calculator(expression: str) -> str:
    """Evaluates mathematical expressions safely."""
    try:
        allowed = set("0123456789+-*/(). ")
        clean_expr = "".join(c for c in expression if c in allowed)
        return str(eval(clean_expr))
    except Exception as e:
        return f"Calculation error: {str(e)}"