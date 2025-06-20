import re

def handle_search(user_input: str) -> str:
    try:
        with open("data/sample.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        results = []
        current_brand = None
        current_price = None

        for line in lines:
            line = line.strip()

            if '"Brand":' in line:
                current_brand = re.sub(r'.*"Brand":\s*"(.*?)",?', r"\1", line)
                current_price = None  # reset

            if '"Selling_Price_INR":' in line:
                current_price = re.sub(r'.*"Selling_Price_INR":\s*(\d+)', r"\1", line)

            # If both brand and price are found, add to results
            if current_brand and current_price:
                results.append(f"{current_brand} → ₹{current_price}")
                current_brand = None
                current_price = None

        return "\n".join(results) if results else "No matching flute data found."

    except Exception as e:
        return f"Search error: {e}"
