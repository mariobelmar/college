# :w|!clear; python %
print('Bonjour')
age = 13
s, l, d = 'hello', [22, 3.14, 'world'], {'age': 33, 'name': 'Luis'}
nom = 'Luis' # input('votre nom: ')
ss = f"""==
    bonjour {nom}
    comment allez vous ?
    =="""

print('=== String ===')
print('== new lines with \"\"\" and \\n ==')
print('Todo: create 3 multilines strings')


s1 = 'xxx'
s2 = 'xxx'
s3 = 'xxx'

print('== f-string ==')

nom, age = 'Mario', 13

ss = (f'l\'élève {nom}...\n'
      f'   a {age} ans')
print(ss)


print('=== Control structures ===')
print('Todo: put in a list ll all __builtins__ python methods, use '
      's.islower and s.startswith')

print(l)
# [22, 3.14, 'world']
for i in l:
    if True:
        print(i)
