import itertools
import math
import time

from termcolor import cprint

from utilities import optimized_prime_sieve


#Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
#           What is the largest prime factor of the number 600851475143 ?

big_number = 600851475143
sqrt_big_number = math.sqrt(big_number)

primes = []

counter = 0
iteration = 0

times = [time.time()]
last = time.time()
algorithm_start = time.time()

for prime in optimized_prime_sieve():
    if (time.time() - algorithm_start) > 60.0:
        break
    counter += 1
    iteration += 1
    current = time.time()
    times.append(current - last)
    last = current

    if len(times) > 1000:
        times.pop(0)

    avg_time = reduce(lambda t1, t2: t1 + t2, times) / len(times)
    rate = 1 / avg_time

    if iteration == 10000:
        cprint('Prime {0}: {1}  {2} p/sec'.format(counter, prime, rate), 'yellow')
        iteration = 0

    primes.append(prime)

total_time = time.time() - algorithm_start

cprint('a total of {} primes were found in {} minutes and {} seconds.'.format(len(primes),
       total_time // 60, total_time % 60), 'blue')

prime_factors = []
for prime in primes:
    if big_number % prime == 0:
        prime_factors.append(prime)

for factor in prime_factors:
    print factor

print max(prime_factors)
