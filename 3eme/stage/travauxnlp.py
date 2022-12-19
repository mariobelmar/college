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

FILES = ["ani_2000_o.txt"]
         # "aari_1994_o.txt",
         # "abun_19952_o.txt",
         # "abu_1985_o.txt",
         # "abun_19952_o.txt",
         # "abun_1999_o.txt",
         # "aari_1990_o.txt",
         # "abun_1995_o.txt"]


def get_text_from_file(file: str) -> str:
    """
    ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
    myfile représente le fichier texte il peut donc en faire plusieurs chose
    """
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def test_all_files(text):
    doc = nlp(text)
    tones1 = [token for token in doc if token.text == 'tone']
    tones2 = [token for token in doc if token.text == 'tones']
    tones = tones1 + tones2
    genders2 = [token for token in doc if token.text == 'gender']
    genders1 = [token for token in doc if token.text == 'genders']
    genders = genders1 + genders2
    return genders, tones


def mediane(liste1):
    a = len(liste1)
    b = int(a/2)
    c = b + 1
    if b // 2 == 1:
        b = sum(liste1[b], liste1[c])/2
    return liste1[b]


def exist_or_not_tones(tones, mediane: int) -> str:
    bad = "this system doesn't exist in this language"
    good = 'this system exist in this language'
    if mediane < tones:
        return good
    return bad


def exist_or_not_genders(genders, mediane: int) -> str:
    bad = "there isn't genders in this language"
    good = 'there is tones in this language'
    if mediane < genders:
        return good
    return bad


def put_all_word_in_table(FILES):
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
                'langue': i,
                'word': mot,
                'word_occurence': occu,
                   }
            lines.append(line)
    return pd.DataFrame(lines)




def put_test_in_table (files):
    lines = []
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        genders, tones = test_all_files(text)
        line1 = {'langue': i,
                 'gender/tone': 'genders',
                 'k.occu': len(genders)}

        line2 = {'langue': i,
                 'gender/tone': 'tones',
                 'k.occu': len(tones)}
        lines.append(line1)
        lines.append(line2)
    return pd.DataFrame(lines)


if __name__ == '__main__':
    test = put_test_in_table(FILES)
    all_word2 = put_all_word_in_table(FILES)
    # all_word2 = (all_word.sort_values(by=("occurence"), ascending=False))
    occu = list(all_word2.word_occurence)
    print(test)
    print('\n')
    print(all_word2)
    median = mediane(occu)
    nb_gender = (int(test.genders))
    answer_gender = exist_or_not_genders(nb_gender, median)
    print(answer_gender)
