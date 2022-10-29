'''
7 kyu
Name: Pull_your_words_together,_man!

https://www.codewars.com//kata/59ad7d2e07157af687000070
Task: Every time that it tries to say a sentence, instead of formatting it in normal English orthography, it just outputs a list of words.

Robbie has pulled multiple all-nighters to get this project finished, and he needs some beauty sleep. So, he wants you to write the last 
part of his code, a sentencify function, which takes the output that the machine gives, and formats it into proper English orthography.

Your function should:

Capitalise the first letter of the first word.
Add a period (.) to the end of the sentence.
Join the words into a complete string, with spaces.
Do no other manipulation on the words.
'''

def sort_by_value_and_index(arr):
    return [arr[1] for arr in sorted(enumerate(arr),key=lambda x:(x[0] + 1) * x[1])]