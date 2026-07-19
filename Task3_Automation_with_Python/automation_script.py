def get_bot_response(user_input):
    """
    Returns the chatbot's response based on the user's input.
    Uses basic rule-based matching (if-elif-else hierarchy).
    """
    # Normalize input: convert to lowercase and strip whitespace
    message = user_input.strip().lower()
    
    # Predefined replies based on user input
    if message in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! How can I help you today?"
        
    elif message in ["how are you", "how are you doing", "how's it going"]:
        return "I'm just a program, but I'm doing great! Thanks for asking. How are you?"
        
    elif message in ["i am fine", "fine", "good", "great", "doing well"]:
        return "That's wonderful to hear!"
        
    elif message in ["what is your name", "who are you", "name"]:
        return "I am a simple rule-based AI chatbot. You can call me Antigravity Chatbot!"
        
    elif message in ["help", "info"]:
        return "I can respond to greeting words (hello, hi), ask how you are, tell you my name, or say goodbye. Try one of those!"
        
    elif message in ["bye", "goodbye", "exit", "quit", "see ya"]:
        return "Goodbye! Have a wonderful day!"
        
    else:
        return "I'm sorry, I don't quite understand that. Try typing 'hello', 'how are you', or 'help'!"

def run_chatbot():
    print("=" * 60)
    print("               WELCOME TO ANTIGRAVITY CHATBOT             ")
    print("      (Type 'bye', 'exit', or 'quit' to end the chat)    ")
    print("=" * 60)
    
    while True:
        # Get input from the user
        try:
            user_msg = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! (Session ended)")
            break
            
        # If input is empty, ignore and ask again
        if not user_msg.strip():
            continue
            
        # Get bot response
        bot_reply = get_bot_response(user_msg)
        
        # Display bot response
        print(f"Chatbot: {bot_reply}")
        
        # Break loop if the user said goodbye
        if user_msg.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break
            
    print("=" * 60)
    print("             Chat Session Finished. Thank you!            ")
    print("=" * 60)

if __name__ == "__main__":
    run_chatbot()