def winner(human, ordi):
    ow = "ordi win"
    ega = "egality"
    hw = "human win"
    if human == 'pa':
        if ordi == 'sc':
            return ow
        if ordi =='pa':
            return ega
        if ordi == 'st':
            return hw
    if human == 'sc':
        if ordi == 'sc':
            return ega
        if ordi == 'pa':
            return ow
        if ordi == 'st':
            return hw
    if human == 'st':
        if ordi == 'sc':
            return hw
        if ordi == 'pa':
            return ow
        if ordi == 'st':
            return ega
    return human, ordi

if __name__ == '__main__':
    print(winner('pa', 'pa'))
    print(winner('pa', 'sc'))
    print(winner('pa', 'st'))
    print(winner('sc', 'pa'))
    print(winner('sc', 'sc'))
    print(winner('sc', 'st'))
    print(winner('st', 'pa'))
    print(winner('st', 'sc'))
    print(winner('st', 'st'))
