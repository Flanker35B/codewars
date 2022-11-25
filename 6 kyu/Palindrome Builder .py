'''
6 kyu
Name: Palindrome Builder
https://www.codewars.com/kata/58efb6ef0849132bf000008f/python
Task: Given a string, add the fewest number of characters possible from the front or back to make it a palindrome.
'''

def build_palindrome(s):
    for n in range(len(s), -1, -1):
        if s[:n] == s[:n][::-1]:
            return s[n:][::-1] + s
        if s[-n:] == s[-n:][::-1]:
            return s + s[:-n][::-1]
    return res