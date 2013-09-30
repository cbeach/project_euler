# Problem 7:  10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

from utilities import optimized_prime_sieve
from termcolor import cprint


for i, p in enumerate(optimized_prime_sieve()):
    prime = p
    if i == 10000:
        cprint('{}, {}'.format(i, p), 'green')
        break
