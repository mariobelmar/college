import spacy
import sys

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")
NOVEL = 'grammartext/aari_1994_o.txt'

files = ["aari_1990_o.txt",
         "aari_1994_o.txt",
         "abu_1985_o.txt",
         # "abun_19952_o.txt",
         # "abun_1995_o.txt",
         # "abun_1999_o.txt",
         "ani_2000_o.txt",]



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

# text = get_text_from_file(NOVEL)
# doc = nlp(text)
# tones = [token for token in doc if token.text == 'tone']
# genders = [token for token in doc if token.text == 'gender']


def test_all_files(files):
    for file in files:
        filename = f'grammartext/{file}'
        text = get_text_from_file(filename)
        doc = nlp(text)
        tones = [token for token in doc if token.text == 'tone']
        genders = [token for token in doc if token.text == 'gender']
        print(f'in {file} : {len(tones)} "tones" and {len(genders)} "gender"')


test_all_files(files)
