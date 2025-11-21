# # Simple Rule-Based Chatbot

# def chatbot():
#     print("Chatbot: Hello! I’m your friendly chatbot. Type 'bye' to exit.\n")
    
#     while True:
#         user_input = input("You: ").lower()  
        
#         if user_input == "hello":
#             print("Chatbot: Hi there!")
#         elif user_input == "how are you":
#             print("Chatbot: I'm fine, thanks! How about you?")
#         elif user_input == "what is your name":
#             print("Chatbot: I'm a simple rule-based chatbot created in Python.")
#         elif user_input == "bye":
#             print("Chatbot: Goodbye! Have a great day!")
#             break
#         else:
#             print("Chatbot: Sorry, I didn’t understand that.")

# chatbot()

import tkinter as tk
from tkinter import scrolledtext

def get_bot_response(user_text):
    user_text = user_text.lower()
    if user_text == "hello":
        return "Hi there! How can I help you?"
    elif user_text == "how are you":
        return "I'm doing great! Thanks for asking."
    elif user_text == "what is your name":
        return "I'm a simple rule-based chatbot created in Python."
    elif user_text == "bye":
        return "Goodbye! Have a wonderful day!"
    else:
        return "Sorry, I didn't understand that."

def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return
    chat_box.insert(tk.END, "You: " + user_text + "\n")
    bot_response = get_bot_response(user_text)
    chat_box.insert(tk.END, "Bot: " + bot_response + "\n\n")
    if user_text.lower() == "bye":
        window.after(1000, window.destroy)
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Chatbot UI")
window.geometry("450x550")
window.resizable(False, False)

chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=55, height=25, font=("Arial", 10))
chat_box.pack(pady=10)
chat_box.config(state=tk.NORMAL)

entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=10, pady=5)

send_btn = tk.Button(window, text="Send", width=8, font=("Arial", 12), command=send_message)
send_btn.pack(side=tk.LEFT)

window.mainloop()