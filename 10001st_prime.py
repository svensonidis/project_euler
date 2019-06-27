# finding the 10001st prime number

i = 11
primes = [2, 3, 5, 7]

def isPrime(num):
    for prime in primes:
        if num % prime == 0:
            return False
    return True

while len(primes) < 10002:        
    if not isPrime(i):
        i = i + 1
    else:
        primes.append(i)

print(primes[10000])
