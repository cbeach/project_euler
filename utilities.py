from termcolor import cprint
import itertools
import time


def prime_sieve(n):
    """Generate all primes up to number n"""

    sieve = range(2, n)
    primes = []

    factor = 2
    while factor < n:
        try:
            factor = sieve.pop(0)
        except IndexError:
            break

        primes.append(factor)
        counter = 2
        while (counter * factor) < n:
            try:
                sieve.remove(counter * factor)
            except ValueError:
                pass  # The number has already been removed
            counter += 1

    return primes


def optimized_prime_sieve():
    """Generate all primes up to number n.  This algorithm was taken from http://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python
       after careful study"""

    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        print q
        print p
        if p is None:
            D[q * q] = p
            yield q
        else:
            x = p + q
            while x not in D and not (x & 1):  # (x & 1) equivalent to x % 2
                x += p
            D[x] = p


def check_prime_sieve():
    """The file 'first_thousand_primes is a list of the first thousand primes (duh) that I downloaded
       from http://primes.utm.edu/lists/small/1000.txt"""

    p = open('first_thousand_primes', 'r')
    primes_oracle = []
    lines = p.readlines()
    for i in lines:
        primes_oracle.append(int(i))

    primes = prime_sieve(primes_oracle[-1] + 1)

    for i, j in enumerate(primes):
        if j != primes_oracle[i]:
            cprint('Incorrect prime! {}, {}'.format(primes_oracle[i], j), 'red')
            return False
        else:
            cprint('{}, {}'.format(primes_oracle[i], j), 'green')
    return True


def time_prime_sieve(iterations=100):
    """Time the prime sieve.  Add 1000 to the max prime every iteration"""

    for i in range(iterations):
        start = time.time()
        primes = list(itertools.takewhile(lambda p: p < (i * 1000), optimized_prime_sieve()))
        t = time.time() - start
        cprint('{}: {}'.format(i * 1000, t), 'yellow')

