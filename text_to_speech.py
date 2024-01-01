import os
import time
import subprocess
import logging
from gtts import gTTS

# Constants
FILE_PATH = 'out/output.mp3'
LANGUAGE = 'en'
TEST_TEXT = 'Hello, this is a text-to-speech example.'

def text_to_speech(text, language=LANGUAGE, file_path=FILE_PATH):
    """
    Convert text to speech and play the generated speech.

    Parameters:
    - text (str): The text to be converted to speech.
    - language (str): The language code for text-to-speech (default is 'en').
    - file_path (str): The file path to save the generated speech (default is 'out/output.mp3').
    """
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=language, slow=False)

        # Save the generated speech to a file
        try:
            tts.save(file_path)
        except Exception as e:
            logging.error(f"Error: File couldn't be created - {e}")

        # Play the generated speech using subprocess
        subprocess.run(['start', file_path], shell=True)
        logging.info("Speech successfully generated and played.")

    except Exception as e:
        logging.error(f"Error: {e}")

def del_file(file_path=FILE_PATH):
    """
    Delete a file if it exists.

    Parameters:
    - file_path (str): The file path to be deleted (default is 'out/output.mp3').
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"File '{file_path}' deleted successfully.")
        else:
            logging.warning(f"File '{file_path}' does not exist.")
    except Exception as e:
        logging.error(f"Error deleting file '{file_path}': {e}")

def call_text_to_speech(text=TEST_TEXT, language=LANGUAGE):
    """
    Function to demonstrate calling text_to_speech from another Python file.
    """
    text_to_speech(text, language, file_path=FILE_PATH)
    
    # Sleep 10s to prevent early deletion
    time.sleep(10)
    
    # Delete the temporary mp3 file
    del_file()

def main():
    """
    Main function to demonstrate usage.
    """
    call_text_to_speech()

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    main()
