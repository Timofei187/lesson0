my_string = input('Введите произвольный текст: ')
print(f'Вы ввели {len(my_string)} символов')
print('В верхнем регистре: ', my_string.upper())
print('В нижнем регистре: ',my_string.lower())
print('Без пробелов: ',my_string.replace(' ', ''))
print('Первый символ: ', my_string[0])
print('Последний символ: ', my_string[-1])