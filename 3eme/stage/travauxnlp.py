"""
              langue gender/tone  k.occu  median_occurence  difference   has?
0     ani_2000_o.txt     genders      16                 1          15   True
1     ani_2000_o.txt       tones       7                 1           6   True
2    aari_1994_o.txt     genders       6                 1           5   True
3    aari_1994_o.txt       tones       0                 1          -1  False
4   abun_19952_o.txt     genders       1                 1           0  False
5   abun_19952_o.txt       tones      44                 1          43   True
6     abu_1985_o.txt     genders      30                27           3   True
7     abu_1985_o.txt       tones       8                27         -19  False
8   abun_19952_o.txt     genders       1                 1           0  False
9   abun_19952_o.txt       tones      44                 1          43   True
10   abun_1999_o.txt     genders       2                 1           1   True
11   abun_1999_o.txt       tones      49                 1          48   True
12   aari_1990_o.txt     genders       6                 1           5   True
13   aari_1990_o.txt       tones       4                 1           3   True
14   abun_1995_o.txt     genders       0                 1          -1  False
15   abun_1995_o.txt       tones       2                 1           1   True
"""
import spacy
# import sys
# import csv
# import numpy as np
import pandas as pd

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")

FILES = ["ani_2000_o.txt",
         "aari_1994_o.txt",
         "abun_19952_o.txt",
         "abu_1985_o.txt",
         "abun_19952_o.txt",
         "abun_1999_o.txt",
         "aari_1990_o.txt",
         "abun_1995_o.txt"]


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


def put_test_in_table (files):
    lines = []
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        doc = nlp(text)
        genders, tones = test_all_files(text)
        liste1 = [token.lemma_ for token in doc if token.pos_ not in ['PUNCT', 'SPACE']]
        pre_median = []
        for t in set(liste1):
            occu = liste1.count(t)
            pre_median.append(occu)
        median = mediane(pre_median)
        gender_diff = len(genders) - median
        tone_diff  = len(tones) - median
        if gender_diff > 0:
            msg1 = True
        else:
            msg1 = False
        if tone_diff > 0:
            msg2 = True
        else:
            msg2 = False
        line1 = {'langue': i[:-4],
                 'gender/tone': 'genders',
                 'k.occu': len(genders),
                 'median_occurence': median,
                 'difference': gender_diff,
                 'has?': msg1}
        line2 = {'langue': i[:-4],
                 'gender/tone': 'tones',
                 'k.occu': len(tones),
                 'median_occurence': median,
                 'difference': tone_diff,
                 'has?': msg2}
        lines.append(line1)
        lines.append(line2)
    return pd.DataFrame(lines)


if __name__ == '__main__':
    test = put_test_in_table(FILES)
    print(test)
