import spacy
import sys

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")
NOVEL = '../../snt/ndm/alice.txt'

# ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
# myfile représente le fichier texte il peut donc en faire plusieurs chose
with open(NOVEL, 'r') as myfile:
    text = myfile.read()
    mots = text.split()

# sample
ltext = text[2000:3000]


def get_only_verbs(ltext: str) -> list[str]:
    doc = nlp(ltext)
    # verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    verbs = []
    for token in doc:
        if token.pos_ == "VERB":
            verbs.append(token.lemma_)
    return verbs

# for 'mot' in doc:
#     if 'nature du mot' == verbe:
#         verbe.append('infinitif du verbe')

verbs = get_only_verbs(ltext)
print(f'==> only verbs: {verbs}')

