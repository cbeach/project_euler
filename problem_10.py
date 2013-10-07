#Problem 10: Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

from termcolor import cprint
from utilities import optimized_prime_sieve

iteration = 0
running_sum = 0
for p in optimized_prime_sieve():
    if p < 2e6:
        running_sum += p
    else:
        cprint(running_sum, 'green')
        break

