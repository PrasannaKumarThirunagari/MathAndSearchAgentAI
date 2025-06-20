import ollama
from Actions.math_action import handle_math
from Actions.search_action import handle_search
from Actions.generate_action import generate_description

class MyAgent:
    def __init__(self):
        self.model = "llama3"

    def classify_intent(self, user_input: str) -> list:
        """
        Uses LLaMA 3 to classify user input into one or more intents:
        - 'math'
        - 'search'
        - 'generate'
        Returns a list of matching intents.
        """
        system_msg = {
    "role": "system",
    "content": (
        "You are an intent classifier. Return one or more of the following intents:\n"
        "- 'math' for arithmetic operations (e.g. 5 + 2)\n"
        "- 'search' for fact lookup, flute info, or price\n"
        "- 'generate' for generating a full product description sentence\n\n"
        "Only return intents in a comma-separated list.\n"
        "Examples:\n"
        "'What is 5 + 2?' → math\n"
        "'Price of C Scale flute' → search\n"
        "'Describe or generate sentence for C Scale' → generate\n"
        "'Who is Einstein and 4 * 7' → search, math"
    )
}

        user_msg = {"role": "user", "content": user_input}
        try:
            response = ollama.chat(model=self.model, messages=[system_msg, user_msg])
            intent_raw = response["message"]["content"].strip().lower()
            intents = [i.strip().replace("'", "") for i in intent_raw.split(",") if i.strip()]
            return intents
        except Exception as e:
            print(f"[ERROR] Intent classification failed: {e}")
            return []

    def handle(self, user_input: str) -> str:
        """
        Determines intent and routes user input to appropriate handler(s).
        """
        intents = self.classify_intent(user_input)
        print(f"[DEBUG] Input: {user_input} → Intents: {intents}")

        responses = []

        # Handle Search
        if "search" in intents:
            responses.append("🔍 Search:\n" + handle_search(user_input))

        # Handle Math
        if "math" in intents:
            if any(char.isdigit() for char in user_input) and any(op in user_input for op in "+-*/x×"):
                responses.append("🧮 Math:\n" + handle_math(user_input))
            elif "price" in user_input.lower() or "cost" in user_input.lower():
                responses.append("🧮 Math:\n" + handle_math("sum of flute prices"))
            else:
                print("[DEBUG] Math intent detected, but no math expression found — skipping math.")

        # Handle Description Generation
        if "generate" in intents:
            scale = None
            user_lower = user_input.lower()
            for s in ["C", "C#", "D", "D#", "E", "F", "F#", "G", "A", "A#", "B"]:
                if f"{s.lower()} scale" in user_lower or f"{s.lower()} flute" in user_lower:
                    scale = s
                    break
            if scale:
                responses.append("🎤 Generate:\n" + generate_description(scale))
            else:
                responses.append("Please specify a scale (e.g., 'C scale') for description.")

        if not responses:
            return "Sorry, I couldn't understand your request."

        return "\n\n".join(responses)
