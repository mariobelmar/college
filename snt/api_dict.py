d.clear      #{'age': 3, '2':4}.clear =>  d = {}
d.get        #{'age': 3, '2':4}.get('2')   =>  4
d.pop        #{'age': 3, '2':4}.pop('age')  =>  3
d.copy       #{'age': 3, '2':4}.copy()  =>  {'age': 3, '2': 4}
d.items      #{'age': 3, '2':4}.items()  =>  [('age', 3), ('2', 4)]
d.values     #{'age': 3}.values()  => ~ [3]
d.keys       #{'age': 3}.keys() =>  ~ [age]
d.setdefault #{'age': 3}.setdefault('a', 4)  =>  {'age': 3, 'a': 4}
d.fromkeys   #d = {'age' : 3}.fromkeys('dc', 'ab')   =>  d= {'d': 'ab', 'c': 'ab'}

