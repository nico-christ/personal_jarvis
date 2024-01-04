import spacy
# Import the matcher
from spacy.matcher import Matcher


patterns = {
    "get_weather_data": ("get_weather", [[{"LOWER": "weather", "POS": "NOUN"}]]),
    "get_web_result": ("search_web", [[{"LEMMA": "search", "POS": "VERB"}, {"OP":"*"}, {"LOWER": "web", "POS": "NOUN"}]]),
    "greet_user": ("greet", [[{"OP": "*"}, {"LOWER": "hello"}, {"OP": "?", "LOWER": "jarvis"}]]),
    "get_current_time": ("", [[{"": "", "": ""}]]),
    "get_current_date": ("", [[{"": "", "": ""}]]),
    "tell_joke": ("", [[{"": "", "": ""}]]),
    "help": ("", [[{"": "", "": ""}]])
}
print (patterns["get_web_result"][0])
TEST_STRING = "This is a test string to see if the spacy model works fine... I want to challange; myself with this@to get better at understanding ai. this will be used if it works. LOL"

nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [{"POS": "VERB"}, {"OP":"+"}, {"POS": "NOUN"}, {"OP":"?"}, {"POS": "NOUN"}]
matcher.add(patterns["greet_user"][0], patterns["greet_user"][1])

doc = nlp("say hello kolo")

matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)