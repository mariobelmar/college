from random import choice
from ipdb import set_trace

GET_NAME = dict(pa='papier', st='pierre', sc='ciseaux')

GAMES_RULES = (("st", "pa", "pa"),
               ("pa", "sc", "sc"),
               ("sc", "st", "st"))


def winner(human: str, ordi: str) -> tuple[str, str]:
    """
    From human and ordi values return the winner choice and the 'Human' or
    'ordi' depending who the winner is.

    e.g.
    >>> winner('pa', 'sc')
    'sc'
    >>>
    >>> winner('pa', 'sc')
    'sc', 'Human'
    >>>
    """
    for v_ordi, v_human, w_choice in GAMES_RULES:
        if human == ordi:
            return 'egality', ''
        elif human == v_human and ordi == v_ordi:
            w_name = 'human' if w_choice == human else 'ordi'
            return w_choice, w_name
        elif human == v_ordi and ordi == v_human:
            w_name = 'human' if w_choice == human else 'ordi'
            return w_choice, w_name
    return '', ''

def show(human, ordi):
    if human == ordi:
        return f"exequo, les deux ont joué la meme chose: {GET_NAME[human]}"
    w_choice, w_name = winner(human, ordi)
    l_name = 'ordi' if w_name == 'human' else 'human'
    l_choice = human if l_name == 'human' else ordi
    set_trace()
    msg = (f"Le gagnant est {w_name} il a jouéé {GET_NAME[w_choice]}, "
           f"{l_name} a joué {GET_NAME[l_choice]}")
    return msg


def get_ordi(human: str, question: str) -> str:
    # we control human is in ("sc", "st", "st")
    while human not in GET_NAME.keys():
        human = input(f'what is your choice [{question}] ? ')
    ordi = choice(['sc', 'st', 'pa'])
    return ordi


if __name__ == '__main__':
    question = "st: pierre, pa: feuille, sc: ciseaux"
    human = input(f'what is your choice [{question}] ? ')
    ordi = get_ordi(human, question)
    out = show(human, ordi)
    print(out)
