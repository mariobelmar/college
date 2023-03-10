print("## grouping string API")
string_api =
# Format case
s.capitalize   #'abcd'.capitalize()  => 'Abcd'
s.upper        #'abcd'.upper()  => 'ABCD'
s.lower        #'ABCD'.lower()  => 'abcd'
s.swapcase     #'ABcd'.swapcase()  => 'abCD'
s.title        #'a B'.title() => 'A B'
s.center       #?

# replace and translate
s.maketrans
s.translate
s.replace

s.endswith     # 'alacl'.endswith('a')  => False
s.startswith   # 'alacl'.startswith('a') => True

s.count     # 'alalcl'.count('a') => 2
s.find      # 'alacl'.find('a') => 0   'alacl'[0] => 'a'
s.rfind     # 'alacl'.rfind('a') => 2   'alacl'[2] => 'a'
s.rindex    # 'alacl'.rindex('a') => 2 'alacl'[2] => 'a'
s.index     # 'alacl'.index('a') => 0   'alacl'[0] => 'a'

s.join   # "/".join(['home', 'mario', 'python']) => 'home/mario/python'
s.split  #'a/b/c/d'.split('/', 2) =>  ['a', 'b', 'c/d']
s.rsplit     #'a/b/c/d'.rsplit('/', 2) => ['a/b', 'c', 'd']
s.splitlines  'ab\ncd\rd'.splitlines() => ['ab', 'cd', 'd']

# strip spaces and tabs
s.strip       #'   abz  '.strip() => 'abz'
s.rstrip      #'   abz  '.rstrip() => '   abz'
s.lstrip      #'   abz  '.lstrip() => 'abz  '

# Work in progress
s.encode
s.zfill
s.casefold
s.ljust
s.rjust
s.partition
s.rpartition
s.expandtabs
s.format
s.format_map

# is ...
s.isalnum     # 'abc123A'.isalnum()  => True
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
print(string_api)


print('\n## s.count, rfind and find')
s = 'bonjour'
print(f"how many 'o' in string '{s}' ?:",  s.count('o'))
# how many 'o' in string 'bonjour' ?: 2


print('\n## s.index and s.count')
s = 'bonjour monsieur h'
# s = 'bonjour'
if s.count('h'):
    print(f'position of h in "{s}":', s.index('h'))
    # position of h in "bonjour monsieur h": 17
else:
    print(f'"h" not present in "{s}"')
    # "h" not present in "bonjour"

print('\n## s.strip')
t = '/home/mario/path/to/my/file.txt'
print(t, '\n',  t.split('/'))
# ['', 'home', 'mario', 'path', 'to', 'my', 'file.txt']
