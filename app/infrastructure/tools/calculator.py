from langchain.tools import tool

@tool(description="Performs mathematical calculations. Use this tool whenever the user asks something involving calculations or numbers.")
def calculate(expression: str) -> str:
    """
    Performs mathematical calculations. Use this tool whenever the user asks something involving calculations or numbers.

    Args:
        expression: The mathematical expression to calculate (e.g., '23 * 34').
    """
    try:
        # it can be 'numexpr' or 'simpleeval'
        print(f"[dev log] called function: {expression}")
        return str(eval(expression, {"__builtins__": None}, {}))
    except Exception as e:
        return f"Calculator Tool Error: {str(e)}"