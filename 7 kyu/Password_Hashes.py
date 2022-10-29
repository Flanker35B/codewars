'''
7 kyu
Name: Ce*s*r*d Strings
https://www.codewars.com//kata/5ff6060ed14f4100106d8e6f
Task: My PC got infected by a strange virus. It only infects my text files and replaces random letters by *, li*e th*s (like this).

Fortunately, I discovered that the virus hides my censored letters inside root directory.

It will be very tedious to recover all these files manually, so your goal is to implement uncensor function that does the hard work automatically.
'''

def uncensor(infected, discovered):
    for i in range(0,len(discovered)):
        infected=infected.replace('*',discovered[i],1)
    return infected