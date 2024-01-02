from text_to_speech import call_text_to_speech as speak
from speech_to_text import call_speech_to_text as record
from basic_functions import *
from datetime import datetime
import logging

def greet_user():
    try:
        speak("Hello, how are you my guy?")
    except Exception as e:
        logging.error(f"An error occurred while greeting user: {e}")

def get_current_time():
    try:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    except Exception as e:
        logging.error(f"An error occurred while getting current time: {e}")

def apologize():
    try:
        speak("Sorry, I didn't understand the command.")
    except Exception as e:
        logging.error(f"An error occurred while apologizing: {e}")

def help(audio_data):
    # List of supported commands
    commands = ["hello", "help", "time"]
    
    # Find all commands present in the audio data
    found_commands = [cmd for cmd in commands if cmd in audio_data]
    
    if found_commands[1]:
        try:
            # Iterate through each found command and provide information
                if found_commands[1] == "hello":
                    speak("The hello command is used for greeting you")
                elif found_commands[1] == "time":
                    speak("The time command tells you the current time")
                elif found_commands[1] == "help":
                    speak("The help command helps you to understand what the other commands do")
        except Exception as e:
            # Handle any errors that may occur during command explanation
            logging.error(f"An error occurred while explaining commands: {e}")
    else:
        try:
            # Apologize if no matching command is found
            apologize()
            logging.warning("No matching command found")
        except Exception as e:
            # Handle any errors that may occur during apology
            logging.error(f"An error occurred while explaining commands: {e}")   

def process_audio_data(audio_data):
    if "hello" in audio_data:
        greet_user()
    elif "help" in audio_data:
        help(audio_data) # //TODO Fix help
    elif "time" in audio_data:
        get_current_time()
    else:
        apologize()

def main():
    try:
        audio_data = record()
        process_audio_data(audio_data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    main()
