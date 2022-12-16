import spacy
import pandas as pd

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")

FILES = ["aari_1994_o.txt"]
         # "abun_1995_o.txt",
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
        for t in set(liste1):
            occu, mot = liste1.count(t), t
            line = {
                'fichier': i,
                'mots': mot,
                'occurence': occu,
                'ratio': occu / len(text)
            }
            lines.append(line)
    return pd.DataFrame(lines)


def mediane(liste1):
    a = len(liste1)
    b = int(a/2)
    c = b + 1
    if b // 2 == 1:
        b = sum(liste1[b], liste1[c])/2
    return liste1[b]


if __name__ == '__main__':
    df = main(FILES)
    df.to_excel('test.xlsx')
    df2 = (df.sort_values(by=("occurence"), ascending=False)) 
    occu = list(df.occurence)
    print(mediane(occu))



