
#Problem 6: The sum of the squares of the first ten natural numbers is,
#
#           12 + 22 + ... + 102 = 385
#           The square of the sum of the first ten natural numbers is,
#
#           (1 + 2 + ... + 10)2 = 552 = 3025
#           Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#
#           Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


n = 100

sum_of_squares = sum([i * i for i in range(1, n + 1)])
square_of_sums = sum(range(n + 1)) ** 2
print sum_of_squares
print square_of_sums

print square_of_sums - sum_of_squares
