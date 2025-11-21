# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! I’m your friendly chatbot. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower()  
        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "what is your name":
            print("Chatbot: I'm a simple rule-based chatbot created in Python.")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn’t understand that.")


chatbot()

