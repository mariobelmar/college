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


s1 = """bonjour je m'ap-
pelle mario"""
print(s1)

s2 =  "bonjour je m'ap-\n"
s2 += "pelle mario"
print(s2)

s3 = ('bonjour je m\'ap-\n'
      'pelle mario')
print(s3)



if s1 == s2 == s3:
    print('Bravo !\n')
else:
    print('\n:(\n')

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
res = []
for s in dir(__builtins__):
    if s.islower():
        if not s.startswith('__'):
            res.append(s)

print(len(res))
print(res)
