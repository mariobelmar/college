"""
$ python travauxnlp.py

in aari_1990_o.txt      genders :   6 |tones:   4 | times:   4| pour_gender: 0.004% | pour_tone:0.003% | pour_time: 0.003%
in aari_1994_o.txt      genders :   6 |tones:   0 | times:   2| pour_gender:     0% | pour_tone:    0% | pour_time:     0%
in abu_1985_o.txt       genders :  27 |tones:   7 | times:  63| pour_gender: 0.003% | pour_tone:0.001% | pour_time: 0.008%
in abun_19952_o.txt     genders :   1 |tones:  39 | times:  54| pour_gender:   0.0% | pour_tone: 0.01% | pour_time: 0.014%
in abun_1995_o.txt      genders :   0 |tones:   1 | times:  89| pour_gender:     0% | pour_tone:    0% | pour_time:     0%
in abun_1999_o.txt      genders :   2 |tones:  44 | times: 145| pour_gender:   0.0% | pour_tone:0.006% | pour_time: 0.021%
in ani_2000_o.txt       genders :  14 |tones:   6 | times:   4| pour_gender: 0.028% | pour_tone:0.012% | pour_time: 0.008%

$
"""
import spacy
# import sys
# import csv
# import numpy as np
import pandas as pd

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")

FILES = ["abun_1995_o.txt",
         "aari_1994_o.txt",
         "abun_19952_o.txt",
         "abu_1985_o.txt",
         "abun_19952_o.txt",
         "abun_1999_o.txt",
         "aari_1990_o.txt",
         "ani_2000_o.txt"]


def get_text_from_file(file: str) -> str:
    """
    ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
    myfile représente le fichier texte il peut donc en faire plusieurs chose
    """
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def get_ratio(tones, genders, text):
    nbtone = len(tones)
    nbgender = len(genders)
    # nbtime = len(times)
    nbword = len(text)
    pour_tone = round(((nbtone / nbword) * 100), 3)
    # pour_time = round(((nbtime / nbword) * 100), 3)
    pour_gender = round(((nbgender / nbword) * 100), 3)
    return pour_tone, pour_gender


def test_all_files(text):
    doc = nlp(text)
    tones1 = [token for token in doc if token.text == 'tone']
    tones2 = [token for token in doc if token.text == 'tones']
    tones = tones1 + tones2
    # times1 = [token for token in doc if token.lemma == 'times']
    # times2 = [token for token in doc if token.lemma == 'time']
    # times = times1 + times2
    genders2 = [token for token in doc if token.text == 'gender']
    genders1 = [token for token in doc if token.text == 'genders']
    genders = genders1 + genders2
    return genders, tones


def get_all_table(FILES):
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


def main(files):
    lines = []
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        genders, tones, = test_all_files(text)
        pour_tone, pour_gender = get_ratio(tones, genders, text)
        line = {
            'file_name': i,
            'tones': len(tones),
            'pour_tones': pour_tone,
            'genders': len(genders),
            'pour_genders': pour_gender,
        }
        lines.append(line)

    return pd.DataFrame(lines)


if __name__ == '__main__':
    table_kw = main(FILES)
    table_at = get_all_table(FILES)
    print(df.head(10))
    tabel_at = main(FILES)
    occu = list(table_al.occurence)
    print(mediane(occu))
    # df.to_excel('output.xlsx')
    # df.to_csv('output.csv')
    # print('output.xlsx done')

