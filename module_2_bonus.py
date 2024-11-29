from os import remove

num = int(input('Введите число '))
pairs = list()


def unique(pairs):
    vrem = list()
    for i in pairs:
        a = sorted(i)
        print(i, a)
        if a not in vrem:
            vrem.append(i)
    return vrem

def find_crat():
    cr = list()
    for i in range(1, num):
        if num % i == 0 and i != 1 and i != 2:
            cr.append(i)
    return cr

def append_crat(crat):
    for num2 in crat:
        create_pairs(num2)

def create_pairs(a):
    for i in range(1, a):
        pairs.append([i, a - i])

create_pairs(num)
print(pairs)
pairs2 = unique(pairs)

crat = find_crat()
append_crat(crat)
print(pairs2, crat)
