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
    if human   == 'sc':
        if ordi == '' 
    return human, ordi

if __name__ == '__main__':
    print(winner('pa', 'pa'))
    print(winner('pa', 'sc'))
    print(winner('pa', 'st'))
