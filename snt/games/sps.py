GAMES_RULES = (("st", "pa", "pa"),
               ("pa", "sc", "sc"),
               ("sc", "st", "st"))

def winner(human, ordi) -> str:
    """
    >>> winner('pa', 'sc')
    'sc'
    >>>
    """
    egal = 'egality'
    for v_ordi, v_human, winner in GAMES_RULES:
        if human == ordi:
            return egal
        if human ==  v_human and ordi == v_ordi:
            return winner
        if human ==  v_ordi and ordi == v_human:
            return winner


def show(human, ordi):
    return f"{winner(human, ordi):15}: human a joué {human}, ordi joué {ordi}"


if __name__ == '__main__':
    values = ['pa', 'st', 'sc']
    for o in values:
        for h in values:
            print(show(o, h))

