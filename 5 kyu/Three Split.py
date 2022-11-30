'''
5 kyu
Name: Simple Fun #44: Three Split

https://www.codewars.com//kata/588833be1418face580000d8
Task: You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut 
the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in 
each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of 
the pieces after cutting. How many ways can you do it?
'''

def three_split(seq):
    need = sum(seq)/3
    res=0
    zum=0
    chet=0
    for i in range(0, len(seq)-1):
        zum+=seq[i]
        if zum == 2* need:
            res+= chet
        if zum==need:
            chet+=1
    return res