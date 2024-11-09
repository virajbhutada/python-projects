# Import the 're' module for regular expressions
import re

# Predefined rules and responses
rules = {
    r'.*(hi|hello|hey|greetings).*': ['Hello!', 'Hi there!', 'Hey!'],
    r'.*(how are you|how are you doing|what\'s up|how\'s it going).*': ['I am just a computer program, so I don\'t have feelings, but I\'m here to assist you!', 'I don\'t have feelings, but I\'m here and ready to help!'],
    r'.*(bye|goodbye|see you|farewell).*': ['Goodbye!', 'See you later!', 'Have a great day!'],
    r'.*(name|your name|who are you).*': ['I am a chatbot created by Codsoft AI Intern, Viraj N. Bhutada.'],
    r'.*(help me|assist me).*': ['Of course! I\'m here to help. What do you need assistance with?', 'Certainly! I can assist you. What do you need help with?'],
    r'.*(joke|tell me a joke).*': [
        'Sure, here\'s a joke: Why did the chicken cross the road? To get to the other side!',
        'Here\'s one: Why don\'t scientists trust atoms? Because they make up everything!',
        'How about this one: Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them!'
    ],
    r'.*(thanks|thank you|appreciate it).*': ['You\'re welcome!', 'No problem, happy to help!', 'Anytime!']
}

# Define chatbot function
def simple_chatbot(user_input):
    # Matching user input with predefined rules (case-insensitive)
    for pattern, responses in rules.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return responses

    # Default response if no match is found
    return ['I\'m sorry, I didn\'t understand that. Can you please rephrase?', 'I didn\'t get that. Can you try again?', 'I\'m not sure what you mean.']

# Cell (Interactive Conversation Function and Conversation Loop):
def interactive_conversation():
    print("Chatbot: Hi! How can I assist you today? (type 'exit' to end)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            restart = input("Chatbot: If you want to chat again, type 'start'. If you want to exit, type 'exit'.\nYou: ")
            if restart.lower() == 'start':
                print("Chatbot: Let's start again!")
            elif restart.lower() == 'exit':
                print("Chatbot: Thank you for chatting with me! I hope I was able to assist you. Have a great day!")
                break
            else:
                print("Chatbot: I'm sorry, I didn't understand that. Please type 'start' to chat again or 'exit' to end.")
        else:
            response = simple_chatbot(user_input)
            print("Chatbot:", response[0])

# Call the interactive conversation function to start chatting
interactive_conversation()

