'''
6 kyu
Name: Break camelCase
https://www.codewars.com//kata/5208f99aee097e6552000148
Task: Given a string, add the fewest number of characters possible from the front or back to make it a palindrome.
'''

def solution(s):
    x=0
    res=''
    for i, letter in enumerate(s):
        if letter.istitle():
            res+=s[x:i]+' '
            x=i
    if x==0:
        res+=s
    else:
        res+=s[x:]
    return res