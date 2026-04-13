"""
simple_chatbot.py
A simple traditional rule-based chatbot for coursework use.
"""

def show_capabilities():
    print("\nChatbot Capabilities:")
    print("1. Respond to greetings")
    print("2. Tell you its name")
    print("3. Explain what it can do")
    print("4. Answer simple date/time style questions")
    print("5. Handle unknown or malformed input")
    print("6. Exit the conversation\n")


def get_response(user_input: str) -> str:
    text = user_input.strip().lower()

    if not text:
        return "I didn't receive any input. Please type something or type 'help'."

    # greetings
    if text in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        return "Hello! How can I help you today?"

    # help / capabilities
    if text in ["help", "capabilities", "what can you do", "menu"]:
        return (
            "I am a simple traditional chatbot. I can respond to greetings, "
            "tell you my name, explain my capabilities, answer a few simple questions, "
            "and handle unknown input."
        )

    # chatbot name
    if "your name" in text or text == "name":
        return "My name is SimpleBot."

    # simple status
    if "how are you" in text:
        return "I am functioning properly. Thanks for asking."

    # creator question
    if "who made you" in text or "who created you" in text:
        return "I was created as a traditional rule-based chatbot project in Python."

    # simple chatbot explanation
    if "what are you" in text or "who are you" in text:
        return "I am a simple chatbot built using traditional rule-based logic."

    # date/time style answers
    if "date" in text:
        return "I am not connected to a live clock, but you can extend me to show the current date."

    if "time" in text:
        return "I am not connected to a live clock, but you can extend me to show the current time."

    # exit
    if text in ["exit", "quit", "bye", "stop"]:
        return "Goodbye! Thanks for chatting with me."

    # malformed / unknown input
    return "Sorry, I did not understand that. Type 'help' to see what I can do."


def main():
    print("Welcome to SimpleBot!")
    print("Type 'help' to see capabilities.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.strip().lower() in ["exit", "quit", "bye", "stop"]:
            break


if __name__ == "__main__":
    main()
