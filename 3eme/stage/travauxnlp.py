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


# def get_only_verbs(ltext: str) -> list[str]:
#     """
#     for 'mot' in doc:
#         if 'nature du mot' == verbe:
#             verbe.append('infinitif du verbe')
#     """
#     doc = nlp(ltext)
#     # verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
#     verbs = []
#     for token in doc:
#         if token.pos_ == "VERB":
#             verbs.append(token.lemma_)
#     return verbs

text = get_text_from_file(NOVEL)
doc = nlp(text)
key1 = 'tone'
key2 = 'gender'
liste1 = [token for token in doc if token.text == key1]
liste2 = [token for token in doc if token.text == key2]


# ltext = text[:10000]
# verbs = sorted(get_only_verbs(ltext))
# verbs_set = sorted(list(set(verbs)))
pour_liste1 = (len(liste1)/len(text)) * 100
pour_liste2 = (len(liste2)/len(text)) * 100
print(liste1)
print(f' in all the file there are {len(text)} words and there are {len(liste1)} times the word \'{key1}\' so the pourcentage is {pour_liste1}%')
print(liste2)
print(f' in all the file there are {len(text)} words and there are {len(liste2)} times the word \'{key2}\' so the pourcentage is {pour_liste1}%')
# print(f'==> all words: {ltext}')
# print(f'==> in ltext there are {len(ltext)} words')
# print(f'==> in this échantillon there are {len(verbs_set)} verbs: {verbs_set}')
# print(f'==> in this text there are {len(text)} numbers of times we saw the word tones: {len(nb_tones)}')


