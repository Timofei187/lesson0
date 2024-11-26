numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = list()
not_primes = list()
is_prime = True
counter = []

for i in numbers:
    if i == 1:
        continue
    for j in numbers:
        if j > i and len(counter) == 2:
            primes.append(i)
            counter.clear()
            break
        elif j > 1 and len(counter) > 2:
            not_primes.append(i)
            counter.clear()
            break
        if i % j == 0:
            counter.append(i)
print('Primes: ', primes)
print('Not Primes: ', not_primes)
