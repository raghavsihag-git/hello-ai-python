import tkinter as tk
from tkinter import scrolledtext

# Chatbot logic
def ai_chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! I'm your AI buddy. How can I help you today?"
    elif "name" in user_input:
        return "You can call me Mini-AI."
    elif "project" in user_input:
        return "You're working on a cool project! Keep building."
    elif "bye" in user_input:
        return "Goodbye! See you soon."
    else:
        return "Hmm... I'm still learning. Try saying something else!"

# Send message function
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_window.insert(tk.END, f"You: {user_input}\n")
    response = ai_chatbot(user_input)
    chat_window.insert(tk.END, f"Mini-AI: {response}\n\n")
    entry.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("Mini-AI Chatbot")
window.geometry("400x450")

chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, font=("Arial", 10))
chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "Mini-AI: Hi! I'm your mini AI assistant. Type 'bye' to exit.\n\n")

entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(padx=10, pady=5, side=tk.LEFT, expand=True)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

window.mainloop()
