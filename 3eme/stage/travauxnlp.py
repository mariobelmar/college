import spacy
import sys

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")
NOVEL = 'grammartext/aari_1990_o.txt'

def get_text_from_file(file: str) -> str:
    """
    ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
    myfile représente le fichier texte il peut donc en faire plusieurs chose
    """
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def get_only_verbs(ltext: str) -> list[str]:
    """
    for 'mot' in doc:
        if 'nature du mot' == verbe:
            verbe.append('infinitif du verbe')
    """
    doc = nlp(ltext)
    # verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    verbs = []
    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.lemma_)
    return verbs


text = get_text_from_file(NOVEL)
ltext = text[:10000]
verbs = sorted(get_only_verbs(ltext))
verbs_set = sorted(list(set(verbs)))
# print(f'==> all words: {ltext}')
print(f'==> only verbs there are {len(verbs)}: {verbs}')
print('\n')
print(f'==> only verbs without repetition there are {len(verbs_set)}: {verbs_set}')


