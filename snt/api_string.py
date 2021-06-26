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


# group string API
string_api = """
s.capitalize
s.upper
s.lower
s.swapcase
s.title
s.center

s.maketrans
s.translate
s.replace

s.encode

s.endswith
s.startswith

s.count
s.find
s.rfind
s.rindex
s.index

s.join
s.split
s.rsplit
s.splitlines

s.strip
s.rstrip
s.lstrip

s.zfill
s.casefold
s.ljust
s.rjust
s.partition
s.rpartition
s.expandtabs
s.format
s.format_map

s.isalnum
s.isalpha
s.isascii
s.isdecimal
s.isdigit
s.isidentifier
s.islower
s.isnumeric
s.isprintable
s.isspace
s.istitle
s.isupper
"""
