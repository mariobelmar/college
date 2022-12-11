import spacy
import sys

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")
NOVEL = '../../snt/ndm/alice.txt'

def get_text_from_file(file: str) -> str:
    """""
    ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
    myfile représente le fichier texte il peut donc en faire plusieurs chose
    """""
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def get_only_verbs(ltext: str) -> list[str]:
    """""
    for 'mot' in doc:
        if 'nature du mot' == verbe:
            verbe.append('infinitif du verbe')
    """""
    doc = nlp(ltext)
    # verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    verbs = []
    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.lemma_)
    return verbs


text = get_text_from_file(NOVEL)
ltext = text[2000:4500]
verbs = get_only_verbs(ltext)
print(f'==> all words: {ltext}')
print(f'==> only verbs: {verbs}')

