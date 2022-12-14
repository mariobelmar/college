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
import sys

# Définir la langue (an)
nlp = spacy.load("en_core_web_sm")
NOVEL = 'grammartext/aari_1994_o.txt'

FILES = ["aari_1990_o.txt",
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


def get_ratio(tones, genders, times, text):
    nbtone = len(tones)
    nbgender = len(genders)
    nbtime = len(times)
    nbword = len(text)
    if nbtone and nbgender and nbtime > 0:
        pour_tone = round(((nbtone / nbword) * 100), 3)
        pour_time = round(((nbtime / nbword) * 100), 3)
        pour_gender = round(((nbgender / nbword) * 100), 3)
    else:
        pour_tone = 0
        pour_gender = 0
        pour_time  = 0
    return pour_tone, pour_gender, pour_time


def test_all_files(text):
    doc = nlp(text)
    tones = [token for token in doc if token.text == 'tone']
    times = [token for token in doc if token.text == 'time']
    genders = [token for token in doc if token.text == 'gender']
    return genders, tones, times


def main(files):
    for i in files:
        filename = f'grammartext/{i}'
        text = get_text_from_file(filename)
        genders, tones, times = test_all_files(text)
        pour_tone, pour_gender, pour_time = get_ratio(tones, genders, times, text)
        print(f'in {i:20} genders : {len(genders):3} |'
              f'tones: {len(tones):3} | times: {len(times):3}| pour_gender: {pour_gender:5}% | pour_tone:'
              f'{pour_tone:5}% | pour_time: {pour_time:5}%' )


if __name__ == '__main__':
    main(FILES)
