from speech_to_text import test
from text_to_speech import call_text_to_speech as speak


def test_speaking():
    speak("Hallo Andre, wie geht es dir?", "de")

def test_recording_from_file():
    test(file_path='files/harvard.wav')

def test_microphone():
    test(use_microphone=True)


if __name__ == '__main__':
    test_speaking()