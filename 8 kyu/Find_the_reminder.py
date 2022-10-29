'''
8 kyu
Name: Freudian translator
https://www.codewars.com//kata/5713bc89c82eff33c60009f7
Task: In this kata, the function will take a string as its argument, and return a string with every word replaced 
by the explanation to everything, according to Freud. Note that an empty string, or no arguments, should return an empty string.
'''

def to_freud(sentence):
    s=""
    if len(sentence)==0:
        return s
    else:
        for i in range(0,sentence.count(' ')+1):
            s+="sex "
        return s[:-1]