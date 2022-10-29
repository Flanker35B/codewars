'''
7 kyu
Name: Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language

https://www.codewars.com//kata/58287977ef8d4451f90001a0
Task: You will be given an array of objects (associative arrays in PHP, tables in COBOL) representing data about 
developers who have signed up to attend the next coding meetup that you are organising.

Your task is to return either:

true if all developers in the list code in the same language; or
false otherwise.
'''

def is_same_language(lst): 
    lan=lst[0]['language']
    for item in lst:
        if item['language']==lan:
            continue
        else:
            return False
    return True