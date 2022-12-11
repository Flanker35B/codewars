'''
4 kyu
Name: Largest Numeric Palindrome

https://www.codewars.com/kata/556f4a5baa4ea7afa1000046
Task: Create a function that finds the largest palindromic number made from the product of at least 2 of the given arguments.

Notes
Only non-negative numbers will be given in the argument
You don't need to use all the digits of the products
Single digit numbers are considered palindromes
Optimization is needed: dealing with ones and zeros in a smart way will help a lot
'''

from collections import Counter


def numeric_palindrome(*args):
    def find_palindrome(arr, value, pos, res):
        for index in range(pos, len(arr)):
            if pos > 0:
                res.append(value * arr[index])
            find_palindrome(arr, value * arr[index], index + 1, res)

    nums = [i for i in args if i not in [0, 1]] + [1] * min(2, args.count(1)) + [0] * min(2, args.count(0))

    total = []
    find_palindrome(nums, 1, 0, total)

    if len(nums) == 1:
        total = nums

    numbers = []
    for num in set(total):
        c = Counter(str(num)).items()

        digits = sorted(c, key=lambda obj: (obj[1] == 1, -int(obj[0])))

        text = ""
        for digit in digits:
            text += digit[0] * (digit[1] // 2)
            if digit[1] == 1:
                break

        c1 = [obj for obj in c if obj[1] % 2]
        digit = max(c1, key=lambda obj: int(obj[0]) * (obj[1] % 2)) if c1 else ['']

        text = "" if text and int(text) == 0 else text

        numbers.append(int(text + digit[0] + text[::-1]))

    return max(numbers) if numbers else 0