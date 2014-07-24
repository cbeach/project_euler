#!/usr/bin/python

import math

#Problem 2: Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#           By starting with 1 and 2, the first 10 terms will be:
#
#                               1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#           By considering the terms in the Fibonacci sequence whose values do not exceed four
#           million, find the sum of the even-valued terms.


def fibonocci(index):
    golden_ratio = 1.61803398875
    f_number = round(golden_ratio ** index / math.sqrt(5))

    return int(f_number)


index = 0
summation = 0
while True:
    fib = fibonocci(index)

    if fib >= 4e6:
        break

    if fib % 2 == 0:
        summation += fib

    index += 1

print summation