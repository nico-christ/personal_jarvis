from text_to_speech import call_text_to_speech as speak
from speech_to_text import call_speech_to_text as record
from basic_functions import *
from datetime import datetime
import logging

def greet_user():
    """Greet the user."""
    try:
        speak("Hello, how are you my guy?")
    except Exception as e:
        logging.error(f"An error occurred while greeting user: {e}")

def get_current_time():
    """Get and speak the current time."""
    try:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    except Exception as e:
        logging.error(f"An error occurred while getting current time: {e}")

def apologize():
    """Apologize for not understanding the command."""
    try:
        speak("Sorry, I didn't understand the command.")
    except Exception as e:
        logging.error(f"An error occurred while apologizing: {e}")

def help(audio_data):
    """
    Provide help for recognized commands.

    Parameters:
    - audio_data (str): The audio data containing user commands.
    """
    # List of supported commands
    commands = ["hello", "help", "time"]
    
    # Find all commands present in the audio data
    found_commands = [cmd for cmd in commands if cmd in audio_data]

    # Check the second entry in found_commands (if it exists)
    if len(found_commands) >= 2:
        try:
            found_command = found_commands[1]  # Get the second entry
            # Provide information based on the found command
            if found_command == "hello":
                speak("The hello command is used for greeting you")
            elif found_command == "time":
                speak("The time command tells you the current time")
            elif found_command == "help":
                speak("The help command helps you to understand what the other commands do")
        except Exception as e:
            # Handle any errors that may occur during command explanation
            logging.error(f"An error occurred while explaining commands: {e}")
    else:
        try:
            # Apologize if no second matching command is found
            apologize()
            logging.warning("No second matching command found")
        except Exception as e:
            # Handle any errors that may occur during apology
            logging.error(f"An error occurred while explaining commands: {e}")

def process_audio_data(audio_data):
    """
    Process the audio data and execute the corresponding command.

    Parameters:
    - audio_data (str): The audio data containing user commands.
    """
    if "help" in audio_data:
        help(audio_data)
    elif "hello" in audio_data:
        greet_user()
    elif "time" in audio_data:
        get_current_time()
    else:
        apologize()

def main():
    """Main function to execute the voice command processing."""
    try:
        audio_data = record()
        process_audio_data(audio_data)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up logging to display only error messages
    logging.basicConfig(level=logging.ERROR)
    main()
