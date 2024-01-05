import spacy
# Import the matcher
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span, Token


patterns = {
    "get_weather_data": ("get_weather", [[{"LOWER": "weather", "POS": "NOUN"}]]),
    "get_web_result": ("search_web", [[{"LEMMA": "search", "POS": "VERB"}, {"OP":"*"}, {"LOWER": "web", "POS": "NOUN"}]]),
    "greet_user": ("greet", [[{"OP": "*"}, {"LOWER": "hello"}, {"OP": "?", "LOWER": "jarvis"}]]),
    "get_current_time": ("", [[{"": "", "": ""}]]),
    "get_current_date": ("", [[{"": "", "": ""}]]),
    "tell_joke": ("", [[{"": "", "": ""}]]),
    "help": ("", [[{"": "", "": ""}]])
}


def process_with_nlp(input: str):
    """
    This method is used to get called from other files to process natural language input.
    It then redirects the data further.
    
    Args:
        input (_type_): _description_
    """
    # Add callable function and further logic
    pass


# ----------------------------- create() functions --------------------------
def create_nlp(language="en_core_web_sm"):
    """
    Create a new spaCy NLP (Natural Language Processing) object for text processing.

    This function initializes a spaCy language model for the specified language 
    and returns an NLP object that can be used for various natural language processing tasks.

    Args:
        input (str): The input text for which the NLP object is created.
        language (str, optional): The language code or model name for the spaCy language model.
            Defaults to "en_core_web_sm".

    Returns:
        spacy.lang.<Language>: A spaCy NLP (Natural Language Processing) object.

    Example:
        >>> nlp = create_nlp("This is a sample text.")
        >>> doc = nlp("This is another text.")
    """
    nlp = spacy.load(language)
    # Some more code
    return nlp

def create_doc(nlp: spacy.Language.component, input: str) -> Doc:
    """
    Create a spaCy Doc object from the input text using a specified spaCy language model.

    Args:
        input_text (str): The input text to be processed.
        nlp (spacy.Language.component): The spaCy language model to be used for processing.

    Returns:
        spacy.tokens.Doc: A spaCy Doc object representing the processed text.

    Example:
        >>> import spacy
        >>> from your_module import create_doc
        >>> nlp = spacy.load("en_core_web_sm")
        >>> text_input = "This is a sample text."
        >>> doc = create_doc(text_input, nlp)
        >>> print(doc.text)
        'This is a sample text.'
    """
    doc = nlp(input)
    return doc

def create_doc_manually(nlp: spacy.Language.component, words: list, spaces: list) -> Doc:
    """
    Create a spaCy Doc object with specified words and spaces.

    This function constructs a spaCy Doc object using the provided spaCy language model (`nlp`).
    It allows you to create a custom Doc object by specifying the words and spaces.

    Args:
        nlp (spacy.Language.component): The spaCy language model or pipeline component.
        words (list): A list of strings representing the individual words in the document.
        spaces (list): A list of boolean values indicating whether a space follows each word.
            The length of the spaces list should be one less than the length of the words list.

    Returns:
        spacy.tokens.Doc: A spaCy Doc object containing the specified words and spaces.

    Example:
        >>> import spacy
        >>> from your_module import create_doc
        >>> nlp = spacy.load("en_core_web_sm")
        >>> words = ["Hello", "world", "!"]
        >>> spaces = [True, False]
        >>> custom_doc = create_doc(nlp, words, spaces)
        >>> print(custom_doc.text)
        Hello world!
    """
    doc = Doc(nlp.vocab, words=words, spaces=spaces)
    return doc

def create_span(doc: Doc, start_index: int = 0, end_index: int = None, label: str = None)-> Span:
    """
    Create a spaCy Doc object with specified words and spaces.

    This function constructs a spaCy Doc object using the provided spaCy language model (`nlp`).
    It allows you to create a custom Doc object by specifying the words and spaces.

    Args:
        nlp (spacy.Language.component): The spaCy language model or pipeline component.
        words (list): A list of strings representing the individual words in the document.
        spaces (list): A list of boolean values indicating whether a space follows each word.
            The length of the spaces list should be one less than the length of the words list.

    Returns:
        spacy.tokens.Doc: A spaCy Doc object containing the specified words and spaces.

    Example:
        >>> import spacy
        >>> from your_module import create_doc
        >>> nlp = spacy.load("en_core_web_sm")
        >>> words = ["Hello", "world", "!"]
        >>> spaces = [True, False]
        >>> custom_doc = create_doc(nlp, words, spaces)
        >>> print(custom_doc.text)
        Hello world!
    """
    if label:
        span = Span(doc, start_index, end_index)
    else:
        span = Span(doc, start_index, end_index, label=label)
    return span

def create_token() -> Token:
    pass

def create_pattern():
    pass

def create_matcher(patterns):
    pass


# ---------------------- get() functions ----------------------------
def get_doc() -> Doc:
    pass

def get_keyword(doc: Doc) -> list:
    """
    Function to excract the keywords from the input. This is used to let the model know how to interprete the input.
    """
    # Add logic for keyword processing
    pass

def get_span() -> Span:
    pass

def get_token(doc: Doc, index: int = None) -> list | Token:
    """
    Retrieve a list of tokens or a specific token from a spaCy Doc object.

    This function takes a spaCy Doc object and either iterates through its tokens to 
    return a list of all tokens or retrieves a specific token if an index is provided.

    Args:
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.
        index (int, optional): The index of the token to retrieve. If None, all tokens are returned.

    Returns:
        list or Token:  If index is provided, returns the specified token; 
                        otherwise, returns a list of spaCy tokens extracted from the provided Doc object.

    Example:
        >>> import spacy
        >>> from your_module import get_token
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = nlp("This is a sample sentence.")
        >>> all_tokens = get_token(doc)
        >>> print(all_tokens)
        [This, is, a, sample, sentence, .]
        >>> specific_token = get_token(doc, index=2)
        >>> print(specific_token)
        a
    """
    
    # if an index is provided, the 
    if index:
        token = doc[index]
        return token
    else:
        tokens = []
        
        for token in doc:
            tokens.append(token)
        return tokens

def get_lexical(type: str, doc: Doc) -> list:
    """
    Get lexical information from a spaCy Doc based on the specified type.

    This function takes a spaCy Doc object and a type string, and returns a list
    containing the specified lexical information for each token in the document.

    Args:
        type (str): The type of lexical information to retrieve.
                    Possible values: "index", "text", "is_alpha", "is_num", "is_punct".
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.

    Returns:
        list: A list containing the requested lexical information for each token in the Doc.

    Raises:
        NameError: If the specified type is not found in the supported types.

    Examples:
        >>> import spacy
        >>> from your_module import get_lexical
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = nlp("This is a sample sentence.")
        >>> indices = get_lexical("index", doc)
        >>> print(indices)
        [0, 1, 2, 3, 4, 5]
        >>> texts = get_lexical("text", doc)
        >>> print(texts)
        ['This', 'is', 'a', 'sample', 'sentence', '.']
    """
    
    def get_index():
        return [token.i for token in doc]
    def get_text():
        return [token.text for token in doc]
    def get_is_alpha():
        return [token.is_alpha for token in doc]
    def get_is_num():
        return [token.like_num for token in doc]
    def get_is_punct():
        return [token.is_punct for token in doc]
    
    lexical_types = {
        "index": get_index,
        "text": get_text,
        "is_alpha": get_is_alpha,
        "is_num": get_is_num,
        "is_punct": get_is_punct
    }
    
    if type in lexical_types:
        result_list = lexical_types[type]()
    else:
        raise NameError(f"Type not found: {type}")
    
    return result_list

# ---------------------------- find() functions -----------------------------
def find_pattern(doc: Doc):
    pass

# ------------------------- predict() functions -------------------------
def predict_part_of_speech(doc: Doc) -> dict:
    text = []
    predictions = []
    
    for token in doc:
        text.append(token.text)
        predictions.append(token.pos_)
    
    if len(text) != len(predictions):
        raise IndexError(f"a and b does not have the same length. Doc: {doc}")
    
    result_dit = dict(zip(text, predictions))
    return result_dit

def predict_syntatic_dependencies(doc: Doc, text: bool = False, prediction: bool = False, dependencies: bool = False, syn_head: bool = False):
    if (text and prediction and dependencies and syn_head) == False:
        raise ValueError(f"No secondary parameter provided. Doc: {doc}")
    pass #TODO predict_syntatic_dependencies

def return_finished_string(doc: Doc):
    """_summary_
    This returns the calculated output(doc) as string. Use this to get the generated answer for the text to speech.
    Args:
        doc (_type_): _description_
    """
    # Add returning function and further logic
    pass

def main():
    words = ["Hello", "World", "!"]
    spaces = [True, False, False]
    
    nlp = create_nlp()
    doc = create_doc(nlp, "She ate pizza")
    
    test = predict_part_of_speech(doc)
    print(test)

# for testing
if __name__ == "__main__":
    main()