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
        if ordi == 'pa': return ow
        if ordi == 'st':
            return ega
    return human, ordi


def show(human, ordi):
    msg = f'human a joué {human}, ordi a joué {ordi}'
    return msg


def show2_0(human, ordi):
    return f"{winner(human, ordi):15}: human a joué {human}, ordi joué {ordi}"


if __name__ == '__main__':
    print(f"{show('pa', 'sc')}: {winner('pa', 'sc')}")
    print('')

    print(show2_0('pa', 'sc'))
    print(show2_0('pa', 'st'))
    print(show2_0('pa', 'sc'))
    print(show2_0('st', 'sc'))
    print(show2_0('st', 'st'))
    print(show2_0('st', 'sc'))
    print(show2_0('sc', 'sc'))
    print(show2_0('sc', 'st'))
    print(show2_0('sc', 'sc'))

