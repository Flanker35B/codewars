'''
5 kyu
Name: Palindrome integer composition

https://www.codewars.com//kata/599b1a4a3c5292b4cc0000d5
Task: The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 
8^2 + 9^2 + 10^2 + 11^2 + 12^2 = 595.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums. Note that 1 = 0^2
 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

Given an input n, find the count of all the numbers less than n that are both palindromic and can be written as the sum 
of consecutive squares.
'''


def values(n):
    nums = set()
    for i in range(1, int(n ** 0.5)):
        val = i * i
        while val < n:
            i += 1
            val += i * i
            if str(val) == str(val)[::-1] and val < n:
                nums.add(val)
    return len(nums)