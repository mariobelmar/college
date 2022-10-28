from random import choice

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
    if human == ordi :
        return f"exequo, les deux ont joué la meme chose: {human}"

    w_choice, w_name = winner(human, ordi)
    l_name = 'ordi' if  w_name == 'human' else 'human'
    l_choice = human if l_name == 'human'  else ordi
    msg =  f"Le gagnant est {w_name} il a jouéé {w_choice}, {l_name} a joué {l_choice}"
    return msg

if __name__ == '__main__':
    human = input('what is your choice ? ')
    ordi = choice(['sc', 'st', 'pa'])
    print(show(human, ordi))
