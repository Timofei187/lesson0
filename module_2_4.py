numbers = [i for i in range(10000, 16000)]
primes = []
not_primes = []

for elem in numbers:
    is_prime = True

    for divider in range(2, int(elem**0.5) + 1):
        if elem % divider == 0:
            is_prime = False
            break
    if is_prime and elem != 1:
        primes.append(elem)
    else:
        not_primes.append(elem)

print('Primes: ', primes)
print('Not Primes: ', not_primes)
