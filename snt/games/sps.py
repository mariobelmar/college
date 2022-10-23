# def winner(human, ordi):
#     ow = "ordi win"
#     ega = "egality"
#     hw = "human win"
#     if human == 'pa':
#         if ordi == 'sc':
#             return ow
#         if ordi =='pa':
#             return ega
#         if ordi == 'st':
#             return hw
#     if human == 'sc':
#         if ordi == 'sc':
#             return ega
#         if ordi == 'pa':
#             return ow
#         if ordi == 'st':
#             return hw
#     if human == 'st':
#         if ordi == 'sc':
#             return hw
#         if ordi == 'pa': return ow
#         if ordi == 'st':
#             return ega
#     return human, ordi


def show(human, ordi):
    """
    use me with:
    print(f"{show('pa', 'sc')}: {winner('pa', 'sc')}")
    """
    msg = f'human a joué {human}, ordi a joué {ordi}'
    return msg


def show2_0(human, ordi):
    return f"{winner(human, ordi):15}: human a joué {human}, ordi joué {ordi}"


if __name__ == '__main__':
    values = ['pa', 'st', 'sc']
    for o in values:
        for h in values:
            print(show2_0(o, h))
