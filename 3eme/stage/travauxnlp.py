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


# def reveal_key_words(ltext: str) -> list[str]:
#     doc = nlp(ltext)
#     for token in doc:
#         if token == 'tone':
#             verbs.append(token)
#     return verbs

liste1 =  []
def reveal_key_words(ltext: str) -> list[str]:
    doc = nlp(ltext)
    for token in doc:
        liste1.append(token)

liste2 = []
for i in liste1:
    liste2.append(i)

text = get_text_from_file(NOVEL)
ltext = text[:10000]
verbs = sorted(get_only_verbs(ltext))
verbs_set = sorted(list(set(verbs)))
reveal_key_words(text[3000:4400])
print(liste2)
# key = 'tone'

# nb_tones = reveal_key_words(text)
# print(f'==> all words: {ltext}')
# print(f'==> in ltext there are {len(ltext)} words')
# print(f'==> in this échantillon there are {len(verbs_set)} verbs: {verbs_set}')
# print(f'==> in this text there are {len(text)} numbers of times we saw the word tones: {len(nb_tones)}')


