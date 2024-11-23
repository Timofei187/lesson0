from gc import collect

immutable_var = (1, "2", [1,2], False, (1,3,5))
print(immutable_var)
immutable_var = [1, "2", [1,2], False, (1,3,5)] # возможно переопределить переменную
print(immutable_var)
immutable_var = (1, "2", [1,2], False, (1,3,5))
#immutable_var[0] = 2 невозможно изменить элемент кортежа
#immutable_var[1] = '3' невозможно изменить элемент кортежа
immutable_var[2][1] = '3' # возможно изменить элемент списка внутри кортежа
print(immutable_var)
# immutable_var[3] = True невозможно изменить элемент кортежа
# immutable_var[4][1] = '3' невозможно изменить элемент кортежа
#immutable_var[4][2] = (2,4,6) невозможно изменить элемент кортежа
mutable_list = [1, "2", [1,2], False, (1,3,5)]
print('mutable_list ',mutable_list)
mutable_list[0] = 2
mutable_list[1] = True
mutable_list[2] = (5,6)
print('new mutable_list ',mutable_list)

collection = {1, '2', 3, False, (1, 3, 5)}
collection.update({'denis': 687, 'Max': 3458})
print(collection)
#print(collection.get('denis'))
a = collection.pop()
print(collection, "a = ", a)

collection2 = {'denis': 1244}
print(collection2.get('denis'))