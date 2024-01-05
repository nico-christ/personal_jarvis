import spacy
import functools
from decorators import *
from spacy.matcher import Matcher
from spacy.tokens import Doc, Span, Token


# Constants
LANGUAGE = "en_core_web_sm"

patterns_config = [
    {"name": "adjective_noun", "rules": [{"POS": "ADJ"}, {"POS": "NOUN"}]},
    {"name": "verb_noun", "rules": [{"POS": "VERB"}, {"POS": "NOUN"}]},
    # Add more patterns as needed
]


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
def create_nlp(language=LANGUAGE):
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

def create_matcher(nlp: spacy.Language.component):
    """
    Create and return a spaCy Matcher object.

    This function initializes a spaCy Matcher object with the vocabulary of the provided spaCy language model.
    The Matcher can be used to define and apply text patterns in a flexible and efficient way.

    Args:
        nlp (spacy.Language.component): A spaCy language model.

    Returns:
        Matcher: A spaCy Matcher object initialized with the vocabulary of the provided language model.

    Example:
        >>> import spacy
        >>> from your_module import create_matcher
        >>> nlp = spacy.load("en_core_web_sm")
        >>> matcher = create_matcher(nlp)
        >>> # Use the matcher to define and apply text patterns
    """
    matcher = Matcher(nlp.vocab)
    return matcher


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
    
    if index is not None:
        try:
            return doc[index]
        except IndexError:
            return None  # Handle index out of range gracefully
    else:
        return [token for token in doc]

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

def get_entity(doc: Doc) -> dict:
    """
    Extract named entities from a spaCy Doc object.

    This function retrieves named entities and their corresponding labels from a spaCy Doc object.

    Args:
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.

    Returns:
        dict: A dictionary where keys are named entity texts and values are their corresponding labels.

    Raises:
        IndexError: Raised if the lengths of text and label lists are not equal.

    Example:
        >>> import spacy
        >>> from your_module import get_entity
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = nlp("Apple Inc. is a technology company.")
        >>> entities = get_entity(doc)
        >>> print(entities)
        {'Apple Inc.': 'ORG'}
    """
    text = [ent.text for ent in doc.ents]
    label = [ent.label_ for ent in doc.ents]
    
    if len(text) != len(label):
        raise IndexError(f"Text and Label does not have the same length. Doc: {doc}")
    
    return dict(zip(text, label))

def get_match_id(doc: Doc, matcher, pattern) -> any:
    """
    Get match IDs using a spaCy Matcher with a specified pattern.

    This function adds a pattern to the spaCy Matcher, processes the provided Doc object, 
    and returns the match IDs.

    Args:
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.
        matcher (spacy.matcher.Matcher): A spaCy Matcher object.
        pattern (list): A list representing the pattern to be matched.

    Returns:
        any: Match IDs generated by the Matcher.

    Example:
        >>> import spacy
        >>> from spacy.matcher import Matcher
        >>> from your_module import get_match_id
        >>> nlp = spacy.load("en_core_web_sm")
        >>> matcher = Matcher(nlp.vocab)
        >>> doc = nlp("Apple Inc. is a technology company.")
        >>> pattern = [{"ENT_TYPE": "ORG"}]
        >>> match_ids = get_match_id(doc, matcher, pattern)
        >>> print(match_ids)
        [(384, 385)]
    """
    matcher.add("test", [pattern])
    match_ID = matcher(doc)
    return match_ID

def get_match_text(doc: Doc, match_ID) -> list:
    """
    Get match text spans using match IDs.

    This function takes a spaCy Doc object and match IDs, and returns a list of 
    text spans corresponding to the matches.

    Args:
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.
        match_ID (list): List of match IDs.

    Returns:
        list: List of spaCy spans corresponding to the matches.

    Example:
        >>> import spacy
        >>> from spacy.matcher import Matcher
        >>> from your_module import get_match_id, get_match_text
        >>> nlp = spacy.load("en_core_web_sm")
        >>> matcher = Matcher(nlp.vocab)
        >>> doc = nlp("Apple Inc. is a technology company.")
        >>> pattern = [{"ENT_TYPE": "ORG"}]
        >>> match_ids = get_match_id(doc, matcher, pattern)
        >>> match_text = get_match_text(doc, match_ids)
        >>> print(match_text)
        [Apple Inc.]
    """
    match_span = [doc[start:end] for match_id, start, end in match_ID]
    return match_span
        

# ---------------------------- find() functions -----------------------------


# ------------------------- predict() functions -------------------------
def predict_part_of_speech(doc: Doc) -> dict:
    """
    Predicts part-of-speech (POS) for each token in a spaCy Doc object.

    Args:
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.

    Returns:
        Dict: A dictionary containing the token text as keys and their corresponding part-of-speech predictions as values.

    Raises:
        IndexError: Raised if the lengths of the token text and POS predictions lists are not equal.

    Example:
        >>> import spacy
        >>> from your_module import predict_part_of_speech
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = nlp("She ate pizza")
        >>> result = predict_part_of_speech(doc)
        >>> print(result)
        {'She': 'PRP', 'ate': 'VBD', 'pizza': 'NN'}
    """
    text = [token.text for token in doc]
    predictions = [token.pos_ for token in doc]
    
    if len(text) != len(predictions):
        raise IndexError(f"a and b does not have the same length. Doc: {doc}")
    
    return dict(zip(text, predictions))

def predict_syntatic_dependencies(doc: Doc, return_text: bool = False, return_prediction: bool = False, return_dependencies: bool = False, return_syn_head: bool = False) -> dict | None:
    """
    Predicts syntactic dependencies for a spaCy Doc object.

    Args:
        doc (spacy.tokens.Doc): A spaCy Doc object representing a processed text.
        return_text (bool, optional): If True, includes the text in the result. Defaults to False.
        return_prediction (bool, optional): If True, includes the part-of-speech predictions in the result. Defaults to False.
        return_dependencies (bool, optional): If True, includes the syntactic dependencies in the result. Defaults to False.
        return_syn_head (bool, optional): If True, includes the syntactic head predictions in the result. Defaults to False.

    Returns:
        Union[Dict, None]: A dictionary containing the selected information based on the provided parameters.
                         Returns None if no secondary parameter is provided.

    Raises:
        ValueError: Raised if no secondary parameter is provided.

    Example:
        >>> import spacy
        >>> from your_module import predict_syntactic_dependencies
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = nlp("She ate pizza")
        >>> result = predict_syntactic_dependencies(doc, return_text=True, return_prediction=True)
        >>> print(result)
        {'She': {'pos': 'PRP', 'dep': 'nsubj', 'syn_head': 'ate'},
         'ate': {'pos': 'VBD', 'dep': 'ROOT', 'syn_head': 'ate'},
         'pizza': {'pos': 'NN', 'dep': 'dobj', 'syn_head': 'ate'}}
    """
    # Check if at least one secondary parameter is provided
    if not (return_text or return_prediction or return_dependencies or return_syn_head):
        raise ValueError(f"At least one secondary parameter should be True. Doc: {doc}")

    result_dict = {}
    
    for token in doc:
        token_dict = {}
        if return_text:
            token_dict['text'] = token.text
        if return_prediction:
            token_dict['pos'] = token.pos_
        if return_dependencies:
            token_dict['dep'] = token.dep_
        if return_syn_head:
            token_dict['syn_head'] = token.head.text

        result_dict[token.text] = token_dict

    return result_dict or None


# ------------------- additional functions -----------------------
def explain(label: str) -> str:
    """
    Provides a human-readable explanation for a spaCy linguistic annotation label.

    Args:
        label (str): The spaCy linguistic annotation label for which an explanation is needed.

    Returns:
        str: A human-readable explanation for the provided spaCy label.

    Example:
        >>> from your_module import explain
        >>> explanation = explain('NN')
        >>> print(explanation)
        'noun'
    """
    return spacy.explain(label)

def return_finished_string(doc: Doc) -> str:
    """_summary_
    This returns the calculated output(doc) as string. Use this to get the generated answer for the text to speech.
    Args:
        doc (_type_): _description_
    """
    # Add returning function and further logic
    pass

@timer
def main():
        
    nlp = create_nlp()
    doc = create_doc(nlp, "Upcomming iPhone X release date leaked")
    matcher = create_matcher(nlp)
    pattern = [{"TEXT": "iPhone"}, {"TEXT":"X"}]
    
    id = get_match_id(doc, matcher, pattern)
    test = get_match_text(doc, id)
    print(test)

# for testing
if __name__ == "__main__":
    main()