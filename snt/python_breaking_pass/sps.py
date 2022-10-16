def winner(human, ordi):
    ow = "ordi win"
    if human == 'pa':
        if ordi == 'sc':
            return ow
    return human, ordi

if __name__ == '__main__':
    print(winner('pa', 'pa'))
    print(winner('pa', 'sc'))
