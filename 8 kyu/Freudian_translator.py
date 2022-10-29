'''
8 kyu
Name: Is n divisible by x and y?
https://www.codewars.com//kata/5545f109004975ea66000086
Task: ICreate a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers
'''

def is_divisible(n,x,y):
    return True if n % x == 0 and n % y == 0 else False