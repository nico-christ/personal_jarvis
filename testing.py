from speech_to_text import test
from text_to_speech import call_text_to_speech as speak
from datetime import datetime

def test_speaking():
    speak("Hallo Alper, wie geht es dir?", "de")

def test_recording_from_file():
    test(file_path='files/harvard.wav')

def test_microphone():
    test(use_microphone=True)

def test_current_time():
    now = datetime.now().strftime("%H:%M")
    speak(f"The current time is {now}")

if __name__ == '__main__':
    test_microphone()