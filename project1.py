#pranesh coddoft project
import re
def get_bot_response(user_input):
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot,but I'm doing great! Thanks for asking."
    elif "your name" in user_input:
        return "I'm your friendy chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"

    elif re.search(r"(weather|temperature)",user_input):
        return "I can't check live weather,yet but it's always sunny in my code!"
    elif re.search(r"(time|date)",user_input):
        return "I don't have a watch,but you can check your system time⏰"
    else:
        return "I didn't understand that.Can you rephrase that ?"
print("🤖 Simple Chatbot (type 'bye' to exit) ")
while True:
    user_message=input("You: ")
    if user_message.lower()=="bye":
        print("Bot: Goodbye!! 👋")
        break
    response=get_bot_response(user_message)
    print("Bot:", response)
