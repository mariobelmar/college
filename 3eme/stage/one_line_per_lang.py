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
from statistics import median
import pandas as pd

# define language (en)
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
    tones = [token for token in doc if token.text in ['tone', 'tones']]
    genders = [token for token in doc if token.text in ['gender', 'genders']]
    return genders, tones


def mediane(words):
    """
    from statistics import median
    """
    mid = int(len(words) / 2)
    mid_more_one = mid + 1

    # if mid odd
    if mid % 2 != 0:
        mid = sum(words[mid], words[mid_more_one]) / 2
    med = words[mid]
    assert med == median(words)
    return med


def put_test_in_table (files):
    lines = []
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        doc = nlp(text)
        genders, tones = test_all_files(text)

        words = [token.lemma_ for token in doc if token.pos_ not in ['PUNCT', 'SPACE']]
        median = mediane([words.count(t) for t in set(words)])

        gender_diff = len(genders) - median
        tone_diff  = len(tones) - median

        line = {'langue': i[:-4],
                'median_occu': median,
                't.occu': len(tones),
                'g.occu': len(genders),
                't.diff': len(tones) - median,
                'has_tone': True if tone_diff > 0 else False,
                'g.diff': len(genders) - median,
                'has_gender': True if gender_diff > 0 else False,
                }
        lines.append(line)
    return pd.DataFrame(lines)


if __name__ == '__main__':
    df = put_test_in_table(FILES)
    df = df.sort_values(by=['t.occu', 'g.occu'], ascending=[True, True])
    df.to_csv('langues_has_gender_tone.csv')
    df.reset_index().to_feather('langues_has_gender_tone.feather')
    print(df)
