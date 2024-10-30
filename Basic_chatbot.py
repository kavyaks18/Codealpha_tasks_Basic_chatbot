import pywhatkit
import datetime
import wikipedia
import pyjokes
import nltk
import random
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources if you haven't already
nltk.download('punkt')

# pre-defined responces
greetings = ["hello", "hi", "greetings", "howdy", "hey"]
responses = {
    "how are you": ["I'm doing well, thank you!", "I'm just a bunch of code, but I'm here to help you!", "Doing great! How about you?"],
    "what is your name": ["I'm a chatbot created to assist you.", "You can call me Chatbot!", "I'm just a chatbot, no specific name!"],
    "what can you do": ["I can have conversations with you, answer questions, and provide information!", "I'm here to chat and assist you with your queries."],
    "default": ["I'm sorry, I don't understand that. Can you rephrase?", "That's interesting! Tell me more.", "Could you elaborate on that?"]
}

# Function to determine if user input is a greeting
def is_greeting(user_input):
    tokens = word_tokenize(user_input.lower())
    for word in tokens:
        if word in greetings:
            return True
    return False
def take_command():
    try:

        command = input("Enter your command :")
        command = command.lower()  # Convert command to lowercase
        # Remove assistant name from command
        for name in ['alexa', 'siri']:
            if name in command:
                command = command.replace(name, '').strip()
                break
    except Exception as e:
        print(f"Error: {e}")  # Print any error that occurs
        return ""
    return command  # Return the cleaned command

# Main function to run the assistant
def run_assistant():
    command = take_command()  # Get the command from the user
    if command:  # Check if the command is not empty
        tokens = word_tokenize(command)  # Tokenize the command for better processing
        
        # Process commands based on keywords
        if 'play' in tokens:
            song = command.replace('play', '').strip()  # Extract song name
            pywhatkit.playonyt(song)  # Play song on YouTube
        elif 'time' in tokens:
            time = datetime.datetime.now().strftime('%I:%M %p')  # Get current time
            print(time)
        elif 'who' in tokens and 'is' in tokens:
            person = command.replace('who is', '').strip()  # Extract person's name
            info = wikipedia.summary(person, sentences=1)  # Get summary from Wikipedia
            print(info)
        elif command in greetings:
            return random.choice(greetings)
        elif 'date' in tokens:
            print('Sorry, I have a headache.')  # Predefined response
        elif 'single' in tokens:
            print('I am in a relationship with WiFi.')  # Predefined response
        elif 'joke' in tokens:
            print(pyjokes.get_joke())  # Tell a joke
        elif 'search' in tokens or 'what' in tokens or 'how' in tokens:
            # Handle search commands
            information = command.replace('search', '').replace('what is', '').replace('how to', '').strip()
            info = wikipedia.summary(information, sentences=1)  # Get summary from Wikipedia
            print(info)
        else:
            print('Please say the command again.')  # Handle unrecognized commands

# Run the assistant in an infinite loop
while True:
    run_assistant()  # Continuously run the assistant
