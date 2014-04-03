from termcolor import cprint
import itertools
import time


def optimized_prime_sieve():
    """Generate all primes up to number n.  This algorithm was taken from http://stackoverflow.com/questions/16004407/a-fast-prime-number-sieve-in-python
       after careful study"""
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):  # (x & 1) equivalent to x % 2
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

    primes = []
    for i, prime in enumerate(optimized_prime_sieve()):
        if prime > primes_oracle[-1]:
            break
        primes.append(prime)

    for i, j in enumerate(primes):
        if j != primes_oracle[i]:
            cprint('Incorrect prime! {}, {}'.format(primes_oracle[i], j), 'red')
        else:
            cprint('{}, {}'.format(primes_oracle[i], j), 'green')


def time_prime_sieve(iterations=100):
    """Time the prime sieve.  Add 1000 to the max prime every iteration"""

    for i in range(iterations):
        start = time.time()
        list(itertools.takewhile(lambda p: p < (i * 1000), optimized_prime_sieve()))
        t = time.time() - start
        cprint('{}: {}'.format(i * 1000, t), 'yellow')


def integer_factorization(n):
    """
    Thanks to http://stackoverflow.com/users/500584/agf for this little algorithm

    """
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1)
                                     if n % i == 0)))


if __name__ == '__main__':
    check_prime_sieve()
