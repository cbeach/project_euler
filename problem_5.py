#Problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
#           without any remainder.  What is the smallest positive number that is evenly divisible
#           by all of the numbers from 1 to 20?

n = 20
seq = sorted(range(n // 2, n + 1), reverse=True)

multiple = seq[-1]

while True:
    not_common = False
    for i in seq:
        if multiple % i != 0:
            not_common = True
            break
    if not_common is False:
        print multiple
        break
    else:
        multiple += seq[-1]
