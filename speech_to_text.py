import speech_recognition as sr

# Constants
FILE_PATH = 'files/harvard.wav'  # Path to the audio file
AMBIENT_NOISE_DURATION = 1 # Determine the duration of the noice filtering. Adjust for diffrent quality.
SHOW_FULL_RESPONSE = False  # Determine the API response of the recognition software. TRUE = full response, FALSE = only most likely answer


def record_audio_file(file_path): # Not longer needed
    """
    Records audio from the specified file path using SpeechRecognition.

    Parameters:
    - file_path (str): Path to the audio file.

    Returns:
    - AudioData: Recorded audio data.
    """
    recognizer = sr.Recognizer()

    # This is the audio interpreter.
    with sr.AudioFile(file_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=AMBIENT_NOISE_DURATION)
        audio_data = recognizer.record(source)

    return audio_data

def recognize_audio():
    """
    Recognizes speech from the given audio data using Google's speech recognition.

    Parameters:
    - audio_data (AudioData): Audio data to be recognized.

    Returns:
    - str: Recognized text.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting noise")
        r.adjust_for_ambient_noise(source, AMBIENT_NOISE_DURATION)
        # Actual 
        print("Say something:")
        audio = r.listen(source)

    said = ""
    try:
        print("Attempting to recognize...")
        said = r.recognize_google(audio, show_all=SHOW_FULL_RESPONSE)
        print("You said: ", said)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return said


def call_speech_to_text():
    """
    Call the main function for speech-to-text conversion.

    Returns:
    - The result of the speech-to-text conversion.
    """
    return main()

def main():
    """
    Main function for processing audio.

    Returns:
        str: Recognized text.
    """
    # Record audio from the microphone
    audio_data = recognize_audio()

    # Print the type of the result
    print(f"Type of result: {type(audio_data)}")
    
    # Print the recognized text or a message if it's empty
    if audio_data:
        print("Recognized text:", audio_data)
    else:
        print("No text was recognized.")
    
    return audio_data

def test(file_path=None, use_microphone=False):
    """
    Recognizes speech from the given audio data using Google's speech recognition.

    Parameters:
    - file_path (str): Path to the audio file. If provided, it will recognize audio from the file.
    - use_microphone (bool): If True, it will use the microphone to capture audio.

    Returns:
    - str: Recognized text.
    """
    if file_path:
        try:
            # Record audio from the specified file
            audio_data = record_audio_file(file_path)

            # Recognize and return the speech from the audio data
            recognized_text = recognize_audio(audio_data)

            # Print the type of the result
            print(f"Type of result: {type(recognized_text)}")

            # Print the recognized text
            print(recognized_text)
        except Exception as e:
            print("Error: {e}")
    elif use_microphone:
        try:
            print("Microphone Testcase:\n")
            
            # Record audio from the microphone
            audio_data = recognize_audio()

            # Print the type of the result
            print(f"Type of result: {type(audio_data)}")

            # Print the recognized text
            print(audio_data)
        except Exception as e:
            print("Error: {e}")
    else:
        raise ValueError("Either 'file_path' or 'use_microphone' must be provided.")


if __name__ == "__main__":
    print("Test case")
    main()
