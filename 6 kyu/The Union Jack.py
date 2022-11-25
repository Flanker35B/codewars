'''
6 kyu
Name: The Union Jack
https://www.codewars.com//kata/5620281f0eeee479cd000020
Task: Your aged grandfather is tragically optimistic about Team GB's chances in the upcoming World Cup, and has enlisted 
you to help him make Union Jack flags to decorate his house with.

Instructions
Write a function which takes as a parameter a number which represents the dimensions of the flag. The flags will always 
be square, so the number 9 means you should make a flag measuring 9x9.
It should return a string of the flag, with 'X' for the red/white lines and '-' for the blue background. It should include 
newline characters so that it's not all on one line.
For the sake of symmetry, treat odd and even numbers differently: odd number flags should have a central cross that is 
only one 'X' thick. Even number flags should have a central cross that is two 'X's thick (see examples below).
'''

from math import ceil
def union_jack(n):
    if not isinstance(n, (int, float)):
        return False
    n = max(7, ceil(n))
    res=s=''
    pol,nech=divmod(n - 1, 2)
    for i in range(0,pol):
        pol_str='-'*i+'X'+'-'*(pol-i-1)
        res+=pol_str+'X'*(nech+1)+pol_str[::-1]+'\n'
    s+=res+('X'*n+'\n')*(nech+1)+res[len(res)-2::-1]
    return s