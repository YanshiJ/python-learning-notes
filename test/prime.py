primes = [ 2, 3 ]

for n in range(5,100,2):
    for p in primes:
        is_prime = True
        if n%p==0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
print(primes)