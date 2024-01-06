from spacy.tokens import Doc
from spacy.language import Language

@Language.component("doc_length")
def doc_length(doc: Doc) -> Doc:
    print("Doc length:", len(doc))
    return doc