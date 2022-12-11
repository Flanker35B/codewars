'''
4 kyu
Name: Zombie Apocalypse: the Last Number Standing

https://www.codewars.com/kata/5d9b52214a336600216bbd0e
Task:  Story: In the realm of numbers, the apocalypse has arrived. Hordes of zombie numbers have infiltrated and are ready
 to turn everything into undead. The properties of zombies are truly apocalyptic: they reproduce themselves unlimitedly 
 and freely interact with each other. Anyone who equals them is doomed. Out of an infinite number of natural numbers, 
 only a few remain. This world needs a hero who leads remaining numbers in hope for survival: The highest number to lead those who still remain.

Briefing: There is a list of positive natural numbers. Find the largest number that cannot be represented as the sum of 
this numbers, given that each number can be added unlimited times. Return this number, either 0 if there are no such 
numbers, or -1 if there are an infinite number of them.
'''


from functools import lru_cache

def survivor(zombies):
    if not zombies: return -1
    nums = sorted(zombies)
    represent = lru_cache(maxsize=None)(lambda x: not x or any(represent(x-y) for y in nums[::-1] if x >= y))
    maxi = nums[-1]
    current = [0]*maxi
    for x in range(0, maxi**2, maxi):
        temp = [current[i] or represent(x+i) for i in range(maxi)]
        if temp == current: return -1
        if all(temp):
            y = next(i for i,v in enumerate(current[::-1]) if not v)
            return max(0, x-y-1)
        current = temp