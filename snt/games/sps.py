GAMES_RULES = (("st", "pa", "pa"),
               ("pa", "sc", "sc"),
               ("sc", "st", "st"))

def winner(human, ordi) -> str:
    """
    >>> winner('pa', 'sc')
    'sc'
    >>>
    >>> winner('pa', 'sc')
    'sc', 'Human'
    >>>
    """
    # return 'sc', 'Human'
    egal = 'egality'
    for v_ordi, v_human, w_choice in GAMES_RULES:
        if human == ordi:
            return egal, None
        if human ==  v_human and ordi == v_ordi:
            w_name = 'human' if w_choice == human else 'ordi'
            return w_choice, w_name
        if human ==  v_ordi and ordi == v_human:
            w_name = 'human' if w_choice == human else 'ordi'
            return w_choice, w_name


def show(human, ordi):
    w_choice, w_name = winner(human, ordi)
    if human == ordi :
        return 'exequo'
    return f"Le gagnant est {w_name} il a jouéé {w_choice}, ordi joué {ordi}"





if __name__ == '__main__':
    values = ['pa', 'st', 'sc']
    for o in values:
        for h in values:
            print(show(o, h))

