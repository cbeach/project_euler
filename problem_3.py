from termcolor import cprint
import itertools
from utilities import optimized_prime_sieve


#Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
#           What is the largest prime factor of the number 600851475143 ?

big_prime = 600851475143

primes = []

counter = 0
iteration = 0

for prime in optimized_prime_sieve():
    if prime > (big_prime // 2):
        break
    primes.append(prime)
    counter += 1
