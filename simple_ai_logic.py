# simple_ai_logic.py

# A basic AI-like script that responds to input
def ai_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hi there! I'm your mini AI assistant."
    elif "project" in user_input.lower():
        return "You're working on something amazing. Keep building!"
    else:
        return "Sorry, I didn't get that. Try asking something else."

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    print("AI:", ai_chatbot(user_input))
