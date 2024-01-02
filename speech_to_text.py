import speech_recognition as sr

# Constants
FILE_PATH = 'files/harvard.wav'  # Path to the audio file
AMBIENT_NOISE_DURATION = 0.1 # Determine the duration of the noice filtering. Adjust for diffrent quality.
SHOW_FULL_RESPONSE = True  # Determine the API response of the recognition software. TRUE = full response, FALSE = only most likely answer


def record_audio(file_path):
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


def recognize_audio(audio_data):
    """
    Recognizes speech from the given audio data using Google's speech recognition.

    Parameters:
    - audio_data (AudioData): Audio data to be recognized.

    Returns:
    - str: Recognized text.
    """
    recognizer = sr.Recognizer()

    try:
        recognized_text = recognizer.recognize_google(audio_data, show_all=SHOW_FULL_RESPONSE)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

    return recognized_text

def call_speech_to_text():
    main()

def main():
    """
    Main function for processing audio.

    Returns:
        str: Recognized text.
    """
    # Record audio from the specified file
    audio_data = record_audio(FILE_PATH)

    # Recognize and return the speech from the audio data
    recognized_text = recognize_audio(audio_data)
    return recognized_text


def test():
    """
    Method for testing purposes only.

    Input: audio file (.wav, .aiff, .aiffc, .flac, etc)

    Output: transcribed voice to console via print method
    """
    # Execute the main function
    recognized_text = main()

    # Print the type of the result
    print(f"Type of result: {type(recognized_text)}")

    # Print the recognized text
    print(recognized_text)


if __name__ == "__main__":
    print("Test case")
    test()