import spacy
from math import floor
from statistics import median
import pandas as pd

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
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def test_all_files(text):
    doc = nlp(text)
    tones = [token for token in doc if token.text in ['tone', 'tones']]
    genders = [token for token in doc if token.text in ['gender', 'genders']]
    return genders, tones


def medianne(ll: list[int]) -> int:
    """
    if even: e.g. l = [1, 7, 6, 0]
                          ^  ^
                          L  R
                          1  2
      median = (L + R)/2
    else:
      # e.g. l = [2, 6, 6 , 30, 5]
                        ^
                        C idx:2
      len(l)/2 == 2.5
      floor(2.x) == 2
      median = l[floor(len(l)/2)]
    """
    liste = ll.copy()
    liste.sort()
    size = len(liste)
    if size % 2 == 0:
        R_idx = int((size / 2))
        L_idx = int((size / 2) - 1)
        median = (liste[L_idx] + liste[R_idx]) / 2
    else:
        mid = int(floor(size/2))
        median = liste[mid]

    return median


def has_key(diff):
        if diff > 1:
             has_key = True
        elif diff < -1:
             has_key = False
        else:
             has_key = None
        return has_key


def get_line(i, name_key, list_key, mediane):
        line = {'langue': i[:-4],
                 'gender/tone': name_key,
                 'k.occu': len(list_key),
                 'median_occurence': mediane,
                 'difference': len(list_key) - mediane,
                 'hasornot': has_key(len(list_key) - mediane)}
        return line


def put_test_in_table (files):
    lines = []
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        doc = nlp(text)
        genders, tones = test_all_files(text)
        words = [token.lemma_ for token in doc if token.pos_ not in ['PUNCT', 'SPACE']]
        mediane = int(medianne([words.count(t) for t in set(words)]))
        gender_diff = int(len(genders) - mediane)
        tone_diff  = int(len(tones) - mediane)
        has_gender = has_key(gender_diff)
        has_tone = has_key(tone_diff)
        line1 = get_line(i, 'gender', genders, mediane)
        line2 = get_line(i, 'tons', tones, mediane)
        lines.append(line1)
        lines.append(line2)
    return pd.DataFrame(lines)


if __name__ == '__main__':
    df = put_test_in_table(FILES)
    cc = ['gender/tone', 'hasornot', 'langue', 'k.occu', 'median_occurence', 'difference']
    df.sort_values(by=['gender/tone', 'difference'])
    df = df.loc[:, cc]
    df.reset_index().to_feather('out2.feather')
    print(df)



