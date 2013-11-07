from termcolor import colored
#Problem 4: Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(p):
    return True if (str(p) == str(p)[::-1] and p != 0) else False


def palindrome_products(min_val, max_val):
    for i in range(min_val, max_val):
        for j in range(min_val, max_val):
            product = i * j
            if is_palindrome(product):
                yield product

max_pal = 0
for p in palindrome_products(100, 1000):
    if p > max_pal:
        pal = colored(p, 'green')
        max_pal = p
        print '{}'.format(pal)
