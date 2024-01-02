import requests
import logging

# ----------- logic functions -----------------
def is_string_in_array(target_string, string_array):
    for s in string_array:
        if s in target_string:
            return True
    return False

def find_string_in_array(target_string, string_array):
    for s in string_array:
        if s in target_string:
            return s
    return None

def is_string_in_array_multi(target_string, string_array, number):
    words = target_string.split()
    count = words.count(string_array)
    
    return count >= number

# --------------------- features --------------------
def get_current_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M")

def get_current_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

def set_reminder(message, timestamp):
    # Implement reminder/notification functionality using a scheduler or other means
    pass

def search_web(query):
    # Implement a function to perform web searches
    pass

def get_current_location():
    # Implement a function to retrieve the current GPS coordinates or location
    pass

def get_weather(api_key='65395f57a253a401cf756d3e72320a04', city=get_current_location()):
    """
    Fetch weather data for a given city using the OpenWeatherMap API.

    Parameters:
    - api_key (str): Your OpenWeatherMap API key. (can be found here: https://home.openweathermap.org/api_keys)
    - city (str): The name of the city for which weather information is requested.

    Returns:
    - dict or None: Weather data in JSON format or None if the request fails.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Adjust units based on preference
    }

    try:
        response = requests.get(base_url, params=params, verify=False) # CHANGE LATER!!! -> verify true
        response.raise_for_status()  # Raise HTTPError for bad responses

        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")

    return None

def convert_currency(amount, from_currency, to_currency):
    # Implement a function to convert currency using an API or predefined rates
    pass

def translate_text(text, source_language, target_language):
    # Implement a function to translate text from one language to another
    pass

def take_note(note):
    # Implement a function to store user notes or create a to-do list
    pass

def get_random_response(responses):
    import random
    return random.choice(responses)

def tell_joke(joke_list):
    # Implement a function to tell funny jokes
    pass