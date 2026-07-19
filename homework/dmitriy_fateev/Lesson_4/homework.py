my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': [1, 2, 3, 4, 5],
           'dict': {'first_key': 'first_meaning', 'second_key': 2, 'third_key': 3.0, 'fourth_key': 4, 5: 'fifth'},
           'set': {1, 'banana', 3.7, 4000, 5}}


my_dict['list'].append(6)
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 6
my_dict['dict'].pop('fourth_key')

my_dict['set'].add(7)
my_dict['set'].pop()

print(my_dict['tuple'][-1])
print(my_dict['list'])
print(my_dict['dict'])
print(my_dict['set'])
print(my_dict)
