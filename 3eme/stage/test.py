import spacy
import pandas as pd

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")

FILES = ["aari_1994_o.txt"]
         # "abun_1995_o.txt"]
         # "abun_19952_o.txt",
         # "abu_1985_o.txt",
         # "abun_19952_o.txt",
         # "abun_1999_o.txt",
         # "aari_1990_o.txt",
         # "ani_2000_o.txt"]


def get_text_from_file(file: str) -> str:
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def main(FILES):
    """
    nom du fichier | mot | occurence

    """
    lines = []
    for i in FILES:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        doc = nlp(text)
        liste1 = [token.lemma_ for token in doc if token.pos_ not in ['PUNCT', 'SPACE']]
        for i in set(liste1):
            occu, mot = liste1.count(i), i
            line = {
                'mots': mot,
                'occurence': occu,
            }
            lines.append(line)
    return pd.DataFrame(lines)


if __name__ == '__main__':
    print(main(FILES))
    # for i in FILES:
    #     filename = f'grammartext/{i}'
    #     text = get_text_from_file(filename)
    #     doc = nlp(text)
    #     mot = text.split()
    #     mots = [token for token in doc] 
    #     print(mots[500:750])
    #     # for i in text:
    #     #     print(i)








