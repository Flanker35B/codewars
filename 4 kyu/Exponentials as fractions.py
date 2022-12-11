'''
4 kyu
Name: Exponentials as fractions

https://www.codewars.com/kata/54f5f22a00ecc4184c000034
Task:  The aim is to calculate exponential(x) (written exp(x) in most math libraries) as an irreducible fraction, the 
numerator of this fraction having a given number of digits.

We call this function expand, it takes two parameters, x of which we want to evaluate the exponential, digits which is 
the required number of digits for the numerator.

The function expand will return an array of the form [numerator, denominator]; we stop the loop in the Taylor expansion 
(see references below) when the numerator has a number of digits >= the required number of digits
'''


def expand(x, digit):
    gcd = lambda m, n: m if not n else gcd(n, m % n)

    if int(x) == x:
        power = 1
    else:
        power = 10 ** len(str(x)[str(x).find('.') + 1:])

    x = int(x * power)
    num = power + x
    den = power
    i = 2

    while (num // gcd(num, den)) // 10 ** (digit - 1) == 0:
        num = num * power * i + x ** i
        den *= power * i
        i += 1

    num, den = num // gcd(num, den), den // gcd(num, den)
    return [num, den]