from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(dict(d))  # Output: {'a': 1, 'b': 2, 'c': 3}

names = defaultdict(list)
names['Ahmed'].append('Ahmed Ali')
names['Ahmed'].append('Ahmed Mohamed')
names['Mona'].append('Mona Mohamed')

print(dict(names))

names = defaultdict(str)
names['Ahmed'] = 'Ahmed Ali'
names['Mona'] = 'Mona Mohamed'   

print(dict(names))

fruits = defaultdict(set)
fruits['Ahmed'].add('Apple')
fruits['Ahmed'].add('Banana') 


fruits['Mona'].add('Orange')
fruits['Mona'].add('Apple')

print(dict(fruits))

cities = defaultdict(tuple)
cities['Ahmed'] = ('Cairo', '02')
cities['Mona'] = ('Alexandria', '03')

print(dict(cities))

