'''
6 kyu
Name: House of cards
https://www.codewars.com//kata/543abbc35f0461d28f000c11
Task: You want to build a standard house of cards, but you don't know how many cards you will need. Write a program 
which will count the minimal number of cards according to the number of floors you want to have. For example, if you want
 a one floor house, you will need 7 of them (two pairs of two cards on the base floor, one horizontal card and one pair 
 to get the first floor).
'''

def house_of_cards(floors):
    if floors>=1:
        tc=2
        pc=2
        for i in range(0,floors):
            pc+=3
            tc+=pc
        return tc
    else:
        raise Error