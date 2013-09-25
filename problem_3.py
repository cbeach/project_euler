from termcolor import cprint
import itertools
import utilities


#Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
#           What is the largest prime factor of the number 600851475143 ?

big_prime = 600851475143

primes = []

counter = 0
iteration = 0
prime = utilities.optimized_prime_sieve()
for q in itertools.islice(itertools.count(3), 0, None, 2):
    cprint(q, 'green')


while prime < (big_prime // 2):
    primes.append(prime)
    prime = utilities.optimized_prime_sieve()
    counter += 1
    if counter == 10000:
        counter = 0
        iteration += 1
        print iteration * 10000



