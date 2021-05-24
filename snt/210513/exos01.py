exo_0 = """
create a function `gender(famille)` that take a famille list like this
[('papa', 'M'), ('mum', 'F'), ('me', 'M'), ('bro', 'M')] and return:
Boys:
    papa
    me
    bro
Girls:
    mum
"""

ll = [('papa', 'M'), ('mum', 'F'), ('me', 'M'), ('bro', 'M')]
print(ll)


def gender(famille):
    print('\nversion_1')
    boys = []
    girls = []
    for t in famille:
        if t[-1] == 'M':
            boys.append(t[0])
        if t[-1] == 'F':
            girls.append(t[0])
    print('boys', boys)
    print('girls', girls)
gender(ll)

def gender2(famille):
    print('\nversion_2')
    boys = [t[0] for t in famille if t[-1] == 'M']
    girls = [t[0] for t in famille if t[-1] == 'F']
    print(f"Boys:")
    for i in boys:
        print(f"\t{i}")
    print(f"Girls:")
    for i in girls:
        print(f"\t{i}")
gender2(ll)

def gender3(famille):
    print('\nversion_3')
    boys = [t[0] for t in famille if t[-1] == 'M']
    girls = [t[0] for t in famille if t[-1] == 'F']
    print(f"Boys:")
    print('    ','\n     '.join(boys))
    print(f"Girls:")
    print('    ','\n     '.join(girls))

gender3(ll)

exo_1 = """
Une année est bissextile si elle est divisible par 4 mais non divisible par
100. Les années divisibles par 400 sont également bissextiles.

Écrire une fonction qui demande à l’utilisateur de saisir une année, et qui
affiche un message pour préciser si cette année est bissextile ou non.
"""

data_structure = """
1. define `ll=[17, 38, 10, 25, 72], puis effectuez les actions suivantes:
    - triez et affichez la liste ;
    - ajoutez l’élément 12 à la liste et affichez la liste ;
    - renversez et affichez la liste;
    - affichez l’indice de l’élément 17 ;
    - enlevez l’élément 38 et affichez la liste;
    - affichez la sous-liste du 2eau 3eélément;
    - affichez la sous-liste du début au 2eélément;
    - affichez la sous-liste du 3eélément à la fin
    - affichez la sous-liste complète de la liste;
    - aaffichez le dernier élément en utilisant un indiçage négatif.

Bien remarquer que certaines méthodes de liste ne retournent rien.
"""
ll = [17, 38, 10, 25, 72]

comprehensive_list = """
2. initialisez truc comme une liste vide, etmachincomme une liste de cinq
   flottants nuls.Affichez ces listes. Utilisez la fonction range() pour
   afficher :
    - les entiers de 0 à 3 ;
    - les entiers de 4 à 7 ;
    - les entiers de 2 à 8 par pas de 2.

Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des élé-ments 3 et 6 àchose.

3. Utilisez une liste en compréhension pour ajouter 3 à chaque élément d’une
   liste d’en-tiers de 0 à 5.

4. Utilisez une liste en compréhension pour ajouter 3 à chaque élément d’une
   liste d’en-tiers de 0 à 5, mais seulement si l’élément est supérieur ou égal
   à 2.

5. Utilisez une liste en compréhension pour obtenir la liste
   ['ad', 'ae',  'bd',  'be',◃'cd',  'ce'] à partir des chaînes"abc"et"de".

Indication: utilisez deux bouclesforimbriquées.
"""
# print("== comprehensive_list")
# print([x for x in range(4)])

