import spacy
import pandas as pd

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")

FILES = ["abun_1995_o.txt",
         # "aari_1994_o.txt",
         # "abun_19952_o.txt",
         # "abu_1985_o.txt",
         # "abun_19952_o.txt",
         # "abun_1999_o.txt",
         # "aari_1990_o.txt",
         "ani_2000_o.txt"]


def get_text_from_file(file: str) -> str:
    """
    ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
    myfile représente le fichier texte il peut donc en faire plusieurs chose
    """
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text



if __name__ == '__main__':
    for i in FILES:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        mots = text.split()
        print(f'lettres: {len(text):8} | mots: {len(mots):8}')

        # for i in text:
        #     print(i)






