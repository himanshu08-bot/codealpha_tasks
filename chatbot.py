# Rule-Based Chatbot with Memory (Name Remembering)

user_name = None  # to store user's name

def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower().strip()
    
    # Greeting variations
    if user_input in ["hello", "hi", "hey"]:
        if user_name:
            return f"Hi {user_name}!"
        else:
            return "Hi there! What's your name?"
    
    # Asking about bot's status
    if user_input in ["how are you", "how r u", "how are u", "what's up"]:
        return "I'm fine, thanks!"
    
    # Exit variations
    if user_input in ["bye", "goodbye", "see you", "exit"]:
        return "Goodbye! Have a nice day!"
    
    # If user introduces their name
    if user_input.startswith("my name is "):
        user_name = user_input.replace("my name is ", "").capitalize()
        return f"Nice to meet you, {user_name}!"
    
    if user_input.startswith("i am "):
        user_name = user_input.replace("i am ", "").capitalize()
        return f"Great to meet you, {user_name}!"
    
    return "Sorry, I don't understand that."

print("Chatbot: Hello! You can say hello, introduce yourself, ask how I am, or say bye to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Chatbot:", response)
    
    if user_message.lower() in ["bye", "goodbye", "see you", "exit"]:
        break
