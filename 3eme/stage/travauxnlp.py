import spacy
import sys

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")
NOVEL = 'grammartext/aari_1994_o.txt'

files = ["aari_1990_o.txt",
         "aari_1994_o.txt",
         "abu_1985_o.txt",
         "abun_19952_o.txt",
         "abun_1995_o.txt",
         "abun_1999_o.txt",
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
    doc = nlp(text)
    tones = [token for token in doc if token.text == 'tone']
    genders = [token for token in doc if token.text == 'gender']
    return genders, tones


def get_ratio(tones, genders, text):
    nbtone = len(tones)
    nbgender = len(genders)
    nbword = len(text)
    if nbtone > 0:
        pour_tone = round(((nbtone / nbword) * 100), 3)
    else:
        pour_tone = 0
    if nbgender > 0:
        pour_gender = round(((nbgender / nbword) * 100), 3)
    else:
        pour_gender = 0
    return pour_tone, pour_gender


for i in files :
    filename = f'grammartext/{i}'
    text = get_text_from_file(filename)
    genders, tones = test_all_files(i)
    pour_tone, pour_gender = get_ratio(tones, genders, text)
    print(f'in {i:20} genders : {len(genders):2} |'
          f'tones: {len(tones):2} | pour_gender: {pour_gender:5}% | pour_tone:'
          f'{pour_tone:5}%')





