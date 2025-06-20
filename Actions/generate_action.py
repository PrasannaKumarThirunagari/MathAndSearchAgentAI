import ollama

def generate_description(scale_name: str) -> str:
    prompt = f"""You are a professional product content writer.
Generate a short marketing sentence for a flute named 'Balaji Flutes {scale_name} Scale Premium'.
Mention quality, ideal use, dimensions, and tone briefly."""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": "You generate product descriptions for musical instruments."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Description generation failed: {e}"
