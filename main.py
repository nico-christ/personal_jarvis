from text_to_speech import call_text_to_speech as speak
from speech_to_text import call_speech_to_text as record
from basic_functions import *
import logging

def greet_user():
    """Greet the user."""
    try:
        speak("Hello, how are you my guy?")
    except Exception as e:
        logging.error(f"An error occurred while greeting user: {e}")

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
    commands = ["date", "hello", "help", "time", "weather"]
    
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
            elif found_command == "date":
                speak("The time command tells you the current date")
            elif found_command == "weather":
                speak("The time command tells you the weather right at the moment")
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

def get_weather_data():
    """
    Get weather data for a predefined city and speak the weather information.

    The function fetches weather data for the specified city (Cologne in this case)
    using the OpenWeatherMap API and speaks the current weather conditions.

    Note: Replace the city with the desired location and make sure to have a valid
    OpenWeatherMap API key configured in the get_weather function.

    Raises:
    - Exception: Any general exception that occurs during the process.

    Example:
    get_weather_data()
    """
    city = "Cologne"  # Replace with the desired city
    try:
        if city:
            weather_data = get_weather(city=city)
            if weather_data:
                temperature = weather_data.get('main', {}).get('temp')
                description = weather_data.get('weather', [{}])[0].get('description')
                if temperature is not None and description:
                    speak(f"The weather in {city} is {description} with a temperature of {temperature} degrees Celsius.")
                else:
                    speak("Sorry, the weather information is incomplete.")
            else:
                speak("Sorry, I couldn't fetch the weather information.")
        else:
                speak("Please specify a city for the weather information.")
    except Exception as e:
        logging.error(f"Error while fetching weather data: {e}")

def get_web_result(query):
    try:
        web_data = search_web(query)
        if web_data:
            try:
                #speak(f"I found the following on the web: {web_data}")
                speak(web_data)
            except Exception as e:
                logging.error(f"An error occurred while tring to provide the web data: {e}")
        else:
            speak(f"Sorry i couldn´t find anything regarding: {query}")
    except Exception as e:
        logging.error(f"An error occurred while atempting searching the web: {e}")

def process_audio_data(audio_data):
    """
    Process the audio data and execute the corresponding command.

    Parameters:
    - audio_data (str): The audio data containing user commands.
    """
    keyword_actions = {
        "hello": greet_user,
        "time": get_current_time,
        "date": get_current_date,
        "weather": get_weather_data,
        "joke": tell_joke,
    }
    
    if "help" in audio_data:
        help(audio_data)
        return

    if "search" in audio_data.lower() and "web" in audio_data.lower():
        try:
            search_web_query = get_string_after_keywords(audio_data, 'search', 'web')
            get_web_result(search_web_query)
        except Exception as e:
            logging.error(f"An error occurred while searching the web: {e}")
            apologize()
        return

    for keyword, action in keyword_actions.items():
        if keyword in audio_data.lower():
            try:
                if callable(action):
                    result = action()
                    if result:
                        speak(result)
                else:
                    action(audio_data)
                return
            except Exception as e:
                logging.error(f"An error occurred: {e}")

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
