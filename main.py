from text_to_speech import call_text_to_speech as speak
from speech_to_text import call_speech_to_text as record

def main():
    try:
        audio_data = record()
        
        try:
            speak(text=audio_data)
        except Exception as e:
            print(f"An error occurred, while text-to-speech: {e}")
        
    except Exception as e:
        print(f"An error occurred, while recording audio: {e}")
    


if __name__ == "__main__":
    main()
