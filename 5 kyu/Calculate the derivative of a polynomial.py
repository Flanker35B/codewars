'''
5 kyu
Name: Calculate the derivative of a polynomial

https://www.codewars.com//kata/56d060d90f9408fb3b000b03
Task: Complete the function that calculates the derivative of a polynomial. A polynomial is an expression like: 3x4 - 2x2 + x - 10
'''

def derivative(eq):
    res = '+'.join([s for s in [derive(w) for w in eq.replace('+', ' ').replace('-', ' -').replace('-x', '-1x').split()] if s])
    return res.replace('+-','-') if res else '0'

def derive(term):
    if 'x' not in term: return ''
    if '^' not in term:    
        return term.split('x')[0] if term.split('x')[0] else '1'
    a, b = [int(w) if w else 1 for w in term.split('x^')]
    a, b = a * b, b - 1
    return ('' if a == 1 else str(a)) + 'x' + ('^' + str(b) if b > 1 else '')