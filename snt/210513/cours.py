# :w|!clear; python %
age = 13
s, l, d = 'hello', [22, 3.14, 'world'], {'age': 33, 'name': 'Luis'}

print('\n=== input ===')
nom = 'Luis' # input('votre nom: ')
ss = f"""==
    bonjour {nom}
    comment allez vous ?
    =="""

print('\n=== String ===')
print('\n== new lines with \"\"\" and \\n ==')
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
    print('\n:(')

print('\n== f-string ==')
nom, age = 'Mario', 13
ss = (f'l\'élève {nom}...\n'
      f'   a {age} ans')
print(ss)

print('\n=== Control structures ===')
print('Todo: put in a list ll all __builtins__ python methods, use '
      's.islower and s.startswith')

x = 'Li'
x = 'Romuald'
nom = x.upper() if len(x) >= 4 else x

print(l)
# [22, 3.14, 'world']
res = []
for s in dir(__builtins__):
    if s.islower():
        if not s.startswith('__'):
            res.append(s)
print(len(res))
print(res[-8:])

print('\n=== Comprehensive list')
print('redo the above with a Comprehensive list')

res2 = [s for s in dir(__builtins__) if s.islower() and not s.startswith('__')]


if res == res2:
    print('Bravo !\n')
else:
    print('\n:(')


age = 18
majeur = True if age >= 18 else False
# True

# for s in ll:
#     print(s.upper())
#     print(f'  {getattr(ll, s).__doc__}')
# 

famille = [('papa', 'M'), ('mom', 'F'), ('bro', 'M'), ('me', 'M')]

def getsex(famille):
    print('boys:')
    for t in famille:
        if t[-1] == 'M':
            print('  ', t[0])
    print('girls:')
    for t in famille:
        if t[-1] == 'F':
            print('  ', t[0])


getsex(famille)

# boys:
#    papa
#    bro
#    me
# girls:
#    mom

