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
    -1.1 triez et affichez la liste ;
    -1.2 ajoutez l’élément 12 à la liste et affichez la liste ;
    -1.3 renversez et affichez la liste;
    -1.4 affichez l’indice de l’élément 17 ;
    -1.5 enlevez l’élément 38 et affichez la liste;
    -1.6 affichez la sous-liste du 2eau 3eélément;
    -1.7 affichez la sous-liste du début au 2eélément;
    -1.8 affichez la sous-liste du 3eélément à la fin
    -1.9 affichez la sous-liste complète de la liste;
    -1.10 affichez le dernier élément en utilisant un indiçage négatif.

Bien remarquer que certaines méthodes de liste ne retournent rien.
"""
ll = [17, 38, 10, 25, 72]
# sort
print('1.1. sorted:', ll.sort(), ll)
print('1.2. :', ll.append(12), ll)
print('1.3. :', ll.reverse(), ll)
print('1.4. :', ll[4])
print('1.5. :',ll.remove(38), ll)
print('1.6. :',ll[1:3])
print('1.7. :',ll[:2])
print('1.8. :',ll[2:])
print('1.9. :',ll)
print('1.10.:',ll[-1])

comprehensive_list = """
2.1  Utilisez la fonction range() pour afficher :

    - les entiers de 0 à 3 ;
    - les entiers de 4 à 7 ;
    - les entiers de 2 à 8 par pas de 2.

2.2 à partir de ll = [0, 1, 2, 3, 4, 5] construire [0, 2, 4]

2.3. Utilisez une liste en compréhension pour ajouter 3 à chaque élément
d’une liste d’en-tiers de 0 à 5.

2.4. Utilisez une liste en compréhension pour ajouter 3 à chaque élément
d’une liste d’en-tiers de 0 à 5, mais seulement si l’élément est
supérieur ou égal à 2.

2.5. Utilisez une liste en compréhension pour obtenir la liste
   ['ad', 'ae',  'bd',  'be', 'cd',  'ce'] à partir des
   chaînes"abc"et"de".

Indication: utilisez deux bouclesforimbriquées.
"""
print("== comprehensive_list")
print([x for x in range(4)])

print('2.1', [i for i in range (4)])
print('2.1', [i for i in  range(4, 8, 1)])
print('2.1', [i for i in  range(2, 8, 2)])
ll = [0, 1,  2, 3, 4, 5]
print('2.2', ll.remove(1), ll.remove(3), ll.remove(5), ll)
res=[i + 3 for i in  range(0, 5)]
print('2.3', res)
res2 = [i + 3 for i in  range(0, 5) if i >= 2]
print('2.4', res2)

alph = []
for i in 'abc':
    for j in 'de':
        print(i + j)
        alph.append(i + j)

print('2.5', alph)

[alph2 + alph3 for alph2 in 'abc' for alph3 in 'de']

print('2.5bis', [alph2 + alph3 for alph2 in 'abc' for alph3 in 'de'])
