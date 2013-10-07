#Problem 16: Power digit sum
#2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2 ** 1000?

from termcolor import cprint

power_number = 2 ** 1000
cprint(power_number, 'yellow')

running_sum = 0
for c in str(power_number):
    running_sum += int(c)
cprint(running_sum, 'green')


