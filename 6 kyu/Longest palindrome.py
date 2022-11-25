'''
6 kyu
Name: Longest palindrome


https://www.codewars.com//kata/5a0178f66f793bc5b0001728
Task: A palindrome is a series of characters that read the same forwards as backwards such as "hannah", "racecar" and "lol".

For this Kata you need to write a function that takes a string of characters and returns the length, as an integer value, 
of longest alphanumeric palindrome that could be made by combining the characters in any order but using each character 
only once. The function should not be case sensitive.


'''

from collections import Counter


def longest_palindrome(st):
    s = Counter(x for x in st.lower() if x.isalnum())
    res = 0
    nc = 0
    for k, n in s.items():
        if n % 2:
            res += n - 1
            nc = 1
        else:
            res += n

    return res + 1 if nc == 1 else res