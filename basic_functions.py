import requests
import logging
import configparser
import re

config = configparser.ConfigParser()
config.read('config.ini')

#Constants
GOOGLE_API_KEY = config['API_KEYS']['GOOGLE_API_KEY']
CUSTOM_SEARCH_ENGINE_ID = config['API_KEYS']['CUSTOM_SEARCH_ENGINE_ID']
REG_FILTER = r'<b>|<\/b>|&nbsp;|;|\.\.\.'
COMMON_FILLER_WORDS = [ # Array of common filler words (these get ignored in some features)
    '<b>', '</b>','a', 'about', 'above', 'across', 'after', 'against', 'all', 'almost', 'along', 'also', 'although',
    'always', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are',
    'around', 'as', 'at', 'back', 'be', 'because', 'before', 'behind', 'below', 'beside', 'between',
    'beyond', 'both', 'but', 'by', 'can', 'could', 'did', 'do', 'does', 'done', 'down', 'during', 'each',
    'either', 'else', 'enough', 'even', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere',
    'few', 'first', 'for', 'four', 'from', 'fuck', 'further', 'get', 'give', 'go', 'had', 'has', 'have', 'he', 'her',
    'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it',
    'its', 'itself', 'just', 'least', 'let', 'like', 'likely', 'little', 'made', 'make', 'many', 'may', 'me',
    'might', 'more', 'most', 'much', 'must', 'my', 'myself', 'necessary', 'never', 'next', 'no', 'nobody',
    'none', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'or',
    'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'people', 'put', 'rather', 'said', 'same',
    'say', 'see', 'seem', 'seemed', 'seeming', 'seems', 'several', 'she', 'shit', 'should', 'show', 'since', 'so', 'some',
    'someone', 'something', 'somewhere', 'still', 'such', 'take', 'than', 'that', 'the', 'their', 'theirs', 'them',
    'themselves', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'this', 'those', 'though', 'three',
    'through', 'throughout', 'to', 'together', 'too', 'top', 'toward', 'two', 'under', 'until', 'unto', 'up', 'upon',
    'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'where', 'whether', 'which', 'while',
    'who', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself',
    'yourselves'
]

# ----------- logic functions -----------------
def is_string_in_array(target_string, string_array):
    """
    Check if any string in the given array is present in the target string.

    Parameters:
    - target_string (str): The string to search within.
    - string_array (list): List of strings to check for presence.

    Returns:
    - bool: True if any string in the array is found in the target string, False otherwise.
    """
    for s in string_array:
        if s in target_string:
            return True
    return False

def find_string_in_array(target_string, string_array):
    """
    Find the first string in the array that is present in the target string.

    Parameters:
    - target_string (str): The string to search within.
    - string_array (list): List of strings to find in the target string.

    Returns:
    - str or None: The first string found in the target string, or None if no match is found.
    """
    for s in string_array:
        if s in target_string:
            return s
    return None

def is_string_in_array_multi(target_string, string_array, number):
    """
    Check if a specific number of strings from the array are present in the target string.

    Parameters:
    - target_string (str): The string to search within.
    - string_array (list): List of strings to check for presence.
    - number (int): The minimum number of strings to be present for the function to return True.

    Returns:
    - bool: True if at least the specified number of strings are found in the target string, False otherwise.
    """
    words = target_string.split()
    count = words.count(string_array)
    
    return count >= number

def concate_string(*args):
    """
    Concatenate multiple strings into a single string.

    Parameters:
    - *args (str): Variable number of strings to concatenate.

    Returns:
    - str: The resulting concatenated string.
    """
    result = ''.join(map(str, args))
    return result

# --------------------- basic -----------------------
def get_string_after_keywords(input, *keywords):
    """
    Extracts a variable part of the input string based on a variable number of keywords.

    Parameters:
    - input_string (str): The input string from which to extract the substring.
    - *keywords (str): Variable number of keywords to search for in the input string.

    Returns:
    - str: The substring that follows the first occurrence of any of the keywords.
           Returns an empty string if none of the keywords are found.

    Example:
    >>> input_str = "This is a sample input string with keywords"
    >>> extract_substring(input_str, "sample", "input")
    ' input string with keywords'

    >>> extract_substring(input_str, "is", "keywords")
    ' a sample input string with '
    """
    last_index = -1  # Initialize to a value indicating no keyword found yet

    for keyword in keywords:
        index = input.find(keyword)
        if index != -1:
            # If the keyword is found, update the last_index
            last_index = max(last_index, index)

    if last_index != -1:
        # If at least one keyword is found, return the substring after the last one
        return input[last_index + len(keywords[-1]):]
    else:
        # If none of the keywords are found, return an empty string
        return ""


# --------------------- features --------------------
def get_current_time():
    """
    Get the current time in HH:MM format.

    Returns:
    - str: The current time formatted as HH:MM.
    """
    from datetime import datetime
    return datetime.now().strftime("%H:%M")

def get_current_date():
    """
    Get the current date in YYYY-MM-DD format.

    Returns:
    - str: The current date formatted as YYYY-MM-DD.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

def set_reminder(message, timestamp):
    # Implement reminder/notification functionality using a scheduler or other means
    pass

def search_web(input):
    """
    Search the web using DuckDuckGo Instant Answer API.

    Parameters:
    - query (str): The search query.

    Returns:
    - str: The search result or an error message.
    """
    def build_payload(query, start=1, num=10, date_restrict='m1', **params):
        """
        Build the payload for the Google Custom Search API request.

        Parameters:
        - query (str): The search query.
        - start (int): The starting index of the result set (default is 1).
        - num (int): The number of results to retrieve (default is 10).
        - date_restrict (str): Date restriction parameter (default is 'm1').
        - **params: Additional parameters.

        Returns:
        - dict: The constructed payload.
        """
        payload = {
            'key': GOOGLE_API_KEY,
            'q': query,
            'cx': CUSTOM_SEARCH_ENGINE_ID
            #'start': start,
            #'num': num,
            #'dateRestrict': date_restrict
        }
        payload.update(params)
        return payload
    
    def make_request(payload):
        """
        Make a request to the Google Custom Search API.

        Parameters:
        - payload (dict): The API request payload.

        Returns:
        - dict: The JSON response from the API.
        """
        response = requests.get("https://www.googleapis.com/customsearch/v1", params=payload)
        if response.status_code != 200:
            raise Exception('Request failed')
        return response.json()
    
    
    # Filter out ignored words from the input query
    filtered_input = [word for word in input.split() if word.lower() not in COMMON_FILLER_WORDS]
    
    # Check if the filtered query is empty
    if not filtered_input:
        raise Exception("Empty query after filtering")
    
    query = ' '.join(filtered_input)
    
    # Set up Google Custom Search API base URL and parameters
    payload = build_payload(query)

    try:
        # Process the JSON response from the API
        search_result = make_request(payload)
        
        print(f"Search result: {search_result}")

        # Extract relevant information from the API response
        if 'items' in search_result and search_result['items']:
            # Assuming the first result has the relevant information
            result = search_result['items'][1]['htmlSnippet']
        else:
            result = "No relevant information found."
            return result
    
        print (result)
        # Remove <b> and </b> tags
        output = re.sub(REG_FILTER, '', result)

        print(output)
        return output # Return the result with leading/trailing whitespaces removed

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        # Handle other request errors
        return f"Request error occurred: {req_err}"



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

if __name__ == "__main__":
    result = search_web("python")
    print(result)