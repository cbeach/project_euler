#Problem 9: Special Pythagorean triplet
#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import sys
from itertools import combinations, ifilter
from termcolor import cprint

#powers = [i for i in enumerate(map(lambda x: x ** 2, xrange(1000)))]
for i in combinations(range(1000), 3):
    if (i[0] ** 2 + i[1] ** 2) == i[2] ** 2:
        print 'Triplet Found!: ({}, {}, {})'.format(i[0], i[1], i[2])
        if sum(i) == 1000:
            cprint('Product: {}'.format(i[0] * i[1] * i[2]), 'green')
            sys.exit(1)


#print len(triplets)


#jprint map(sum, triplets)
