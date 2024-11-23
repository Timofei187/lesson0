my_dict = {'den':123,'alex': 234, 'max': 345}
print("My_DICT ", my_dict)
print(my_dict['den'], my_dict.get('oops', 'unavailable'))
my_dict.update({'tim': 456, 'bob': 567})
pop_ = my_dict.pop('alex')
print(pop_)
print(my_dict)

my_set = {1, '2', 3, False, (1, 3, 5), False, 3, 2, 1}
print('My_SET ', my_set)
my_set.add(5)
my_set.add( 'boolean')
my_set.discard('2')
print(my_set)