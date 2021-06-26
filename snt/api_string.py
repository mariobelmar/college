'bonjour'.count('2')
'bonjour'.count('l')
# 0
# 2

'bonjour'.find('2')
'bonjour'.find('l')
# -1
# 2

'bonjour'.rfind('2')
'bonjour'.rfind('l')

s = 'bonjour monsieur h'
# s = 'bonjour'
if s.count('h'):
    print(f'position of h in "{s}":', s.index('h'))
    # position of h in "bonjour monsieur h": 17
else:
    print(f'"h" not present in "{s}"')
    # "h" not present in "bonjour"

'bonjour'.isalnum()
'bonjour'.isalnum()

'bonjour'.isalpha()
'bonjour'.isalpha()

t = '/home/mario/path/to/my/file.txt'
print(t.split('/'))
# ['', 'home', 'mario', 'path', 'to', 'my', 'file.txt']

