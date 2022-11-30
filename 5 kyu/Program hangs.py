'''
5 kyu
Name: Program hangs!

https://www.codewars.com//kata/55f9439929875c58a500007a
Task: Your mission, should you choose to accept it, is to create a new function called wrap_mystery that returns the same
 results as mystery, but does not hang. Since you're not sure exactly what values mystery should be returning for hangs, 
 just have wrap_mystery return -1 for problematic input. Your customer is counting on you!
'''


from signal import *

def handler(signum, frame):
    raise Exception

def wrap_mystery(n):
    signal(SIGALRM, handler)
    setitimer(ITIMER_REAL, .01)
    try: return mystery(n)
    except: return -1