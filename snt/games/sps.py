from random import choice

GET_NAME = dict(pa='papier', st='pierre', sc='ciseaux')

GAMES_RULES = (("st", "pa", "pa"),
               ("pa", "sc", "sc"),
               ("sc", "st", "st"))


def winner(human, ordi) -> tuple[str, str]:
    """
    >>> winner('pa', 'sc')
    'sc'
    >>>
    >>> winner('pa', 'sc')
    'sc', 'Human'
    >>>
    """
    for v_ordi, v_human, w_choice in GAMES_RULES:
        if human == ordi:
            return 'egality', None
        elif human == v_human and ordi == v_ordi:
            w_name = 'human' if w_choice == human else 'ordi'
            return w_choice, w_name
        elif human == v_ordi and ordi == v_human:
            w_name = 'human' if w_choice == human else 'ordi'
            return w_choice, w_name
        else:
            return None, None

def show(human, ordi):
    if human == ordi:
        return f"exequo, les deux ont joué la meme chose: {GET_NAME[human]}"

    w_choice, w_name = winner(human, ordi)
    l_name = 'ordi' if w_name == 'human' else 'human'
    l_choice = human if l_name == 'human' else ordi
    msg = (f"Le gagnant est {w_name} il a jouéé {GET_NAME[w_choice]}, "
           f"{l_name} a joué {GET_NAME[l_choice]}")
    return msg


if __name__ == '__main__':
    question= "st: pierre, pa: feuille, sc: ciseaux"
    human = input(f'what is your choice [{question}] ? ')

    # on control que human est bien dans la list ("sc", "st", "st")

    ordi = choice(['sc', 'st', 'pa'])
    print(show(human, ordi))
