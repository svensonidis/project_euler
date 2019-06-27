# Initialize a list
primes = []
for possiblePrime in range(2, 600851475143):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
      
    if isPrime:
        primes.append(possiblePrime)

listLen = len(primes)

lasrgestPrime = 0
for i in range(0,listLen):
    if 600851475143 % primes[i] == 0:
        lasrgestPrime = primes[i]
    
print(lasrgestPrime)
