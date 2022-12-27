import spacy
from statistics import median
import pandas as pd

nlp = spacy.load("en_core_web_sm")

FILES = ["ani_2000_o.txt",
         "aari_1994_o.txt",
         "abun_19952_o.txt",
         # "abu_1985_o.txt",
         # "abun_19952_o.txt",
         # "abun_1999_o.txt",
         "aari_1990_o.txt",
         "abun_1995_o.txt"]


def get_text_from_file(file: str) -> str:
    with open(file, 'r') as myfile:
        text = myfile.read()
    return text


def test_all_files(text):
    doc = nlp(text)
    tones = [token for token in doc if token.text in ['tone', 'tones']]
    genders = [token for token in doc if token.text in ['gender', 'genders']]
    return genders, tones

def medianne(liste1):
    liste2 = sorted(liste1)
    nb = len(liste1)
    mid = int(nb/2)
    mid1 = mid + 1
    if not nb % 2 == 0:
        mid = int((liste2[mid] + liste2[mid1]) / 2)
    return liste2[mid]


def put_test_in_table (files):
    lines = []
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        doc = nlp(text)
        genders, tones = test_all_files(text)
        words = [token.lemma_ for token in doc if token.pos_ not in ['PUNCT', 'SPACE']]
        mediane = medianne([words.count(t) for t in set(words)])
        gender_diff = int(len(genders) - mediane)
        tone_diff  = int(len(tones) - mediane)
        if gender_diff > 1:
             has_gender = True
        elif gender_diff < -1:
             has_gender = False
        else:
             has_gender = None

        if tone_diff > 1:
             has_tone = True
        elif tone_diff < -1:
             has_tone = False
        else:
             has_tone = None

        line1 = {'langue': i[:-4],
                 'gender/tone': 'genders',
                 'k.occu': len(genders),
                 'median_occurence': mediane,
                 'difference': gender_diff,
                 'hasornot': has_gender}

        line2 = {'langue': i[:-4],
                 'gender/tone': 'tones',
                 'k.occu': len(tones),
                 'median_occurence': mediane,
                 'difference': tone_diff,
                 'hasornot': has_tone}

        lines.append(line1)
        lines.append(line2)
    return pd.DataFrame(lines)


if __name__ == '__main__':
    test = put_test_in_table(FILES)
    print(test)

# medianne
         # langue gender/tone  k.occu  median_occurence  difference hasornot
# 0    ani_2000_o     genders      16                 1          15     True
# 1    ani_2000_o       tones       7                 1           6     True
# 2   aari_1994_o     genders       6                 1           5     True
# 3   aari_1994_o       tones       0                 1          -1     None
# 4  abun_19952_o     genders       1                 2          -1     None
# 5  abun_19952_o       tones      44                 2          42     True
# 6   aari_1990_o     genders       6                 1           5     True
# 7   aari_1990_o       tones       4                 1           3     True
# 8   abun_1995_o     genders       0                 1          -1     None
# 9   abun_1995_o       tones       2                 1           1     None
# mediane
#           langue gender/tone  k.occu  median_occurence  difference hasornot
#  0    ani_2000_o     genders      16               1.0          15     True
#  1    ani_2000_o       tones       7               1.0           6     True
#  2   aari_1994_o     genders       6               1.0           5     True
#  3   aari_1994_o       tones       0               1.0          -1     None
#  4  abun_19952_o     genders       1               2.0          -1     None
#  5  abun_19952_o       tones      44               2.0          42     True
#  6   aari_1990_o     genders       6               1.0           5     True
#  7   aari_1990_o       tones       4               1.0           3     True
#  8   abun_1995_o     genders       0               2.0          -2    False
#  9   abun_1995_o       tones       2               2.0           0     None


