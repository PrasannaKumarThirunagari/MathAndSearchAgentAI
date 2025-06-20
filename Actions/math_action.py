import re

def handle_math(expression: str) -> str:
    try:
        # Lowercase for uniform parsing
        expression = expression.lower()

        # Replace common math words with operators
        replacements = {
            "plus": "+",
            "minus": "-",
            "multiply": "*",
            "multiplied by": "*",
            "times": "*",
            "x": "*",
            "divided by": "/",
            "divide": "/",
            "over": "/",
            "what is": "",
            "equals": "",
            "=": "",
        }

        for word, symbol in replacements.items():
            expression = expression.replace(word, symbol)

        # Remove any non-math characters
        math_expr = re.findall(r"[0-9\+\-\*/\.\(\)\s]+", expression)
        math_expr = "".join(math_expr).strip()

        if not math_expr:
            return "Math Error: No valid expression found."

        result = eval(math_expr)
        return f"The result is {result}"
    except Exception as e:
        return f"Math Error: {e}"
