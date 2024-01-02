from text_to_speech import call_text_to_speech as speak
from speech_to_text import call_speech_to_text as record
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

def process_audio_data(audio_data):
    if "hello" in audio_data:
        greet_user()
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
