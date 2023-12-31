import os
import time
import subprocess
import logging
from gtts import gTTS

"""
Further documentation on gTTs: https://gtts.readthedocs.io/en/latest/
"""

# Dictionaries
languages = {
    'Afrikaans': 'af',
    'Arabic': 'ar',
    'Bulgarian': 'bg',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Catalan': 'ca',
    'Czech': 'cs',
    'Danish': 'da',
    'German': 'de',
    'Greek': 'el',
    'English': 'en',
    'Spanish': 'es',
    'Estonian': 'et',
    'Finnish': 'fi',
    'French': 'fr',
    'Gujarati': 'gu',
    'Hindi': 'hi',
    'Croatian': 'hr',
    'Hungarian': 'hu',
    'Indonesian': 'id',
    'Icelandic': 'is',
    'Italian': 'it',
    'Hebrew': 'iw',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Khmer': 'km',
    'Kannada': 'kn',
    'Korean': 'ko',
    'Latin': 'la',
    'Latvian': 'lv',
    'Malayalam': 'ml',
    'Marathi': 'mr',
    'Malay': 'ms',
    'Myanmar (Burmese)': 'my',
    'Nepali': 'ne',
    'Dutch': 'nl',
    'Norwegian': 'no',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Albanian': 'sq',
    'Serbian': 'sr',
    'Sundanese': 'su',
    'Swedish': 'sv',
    'Swahili': 'sw',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Filipino': 'tl',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Vietnamese': 'vi',
    'Chinese (Simplified)': 'zh-CN',
    'Chinese (Mandarin/Taiwan)': 'zh-TW',
    'Chinese (Mandarin)': 'zh'
}

# Constants
FILE_PATH = 'out/output.mp3'
LANGUAGE = "en-US" #languages["English"]
TEST_TEXT = 'Hello, this is a text-to-speech example.'
SLEEP_TIME = 10

def custom_voice():
    # Create function for custom voice
    pass

def text_to_speech(text, language=LANGUAGE, file_path=FILE_PATH, voice=None):
    """
    Convert text to speech and play the generated speech.

    Parameters:
    - text (str): The text to be converted to speech.
    - language (str): The language code for text-to-speech (default is 'en').
    - file_path (str): The file path to save the generated speech (default is 'out/output.mp3').
    """
    
    if voice:
        try:
            custom_voice()
        except Exception as e:
            logging.error(f"Error with custom voice: {e}")
    else:
    
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
    
    # Sleep to prevent early deletion
    time.sleep(SLEEP_TIME)
    
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
