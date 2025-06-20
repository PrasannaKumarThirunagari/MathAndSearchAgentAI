try:
    from agents import MyAgent
except ImportError:
    print("❌ Error: Could not import MyAgent. Make sure agent.py is in the same folder.")
    MyAgent = None

if __name__ == "__main__":
    if MyAgent:
        agent = MyAgent()
        print("🤖 LLaMA 3 Local Agent (Math + Search) Started. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            response = agent.handle(user_input)
            print("Agent:", response)
    else:
        print("Program terminated due to missing agent.")
