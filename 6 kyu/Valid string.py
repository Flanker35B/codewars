'''
6 kyu
Name: Valid string

https://www.codewars.com//kata/52f3bb2095d6bfeac2002196
Task: You are given a sequence of valid words and a string. Test if the string is made up by one or more words from the array.

Task
Test if the string can be entirely formed by consecutively concatenating words of the dictionary.
'''

def valid_word(seq, word):
    if len(word) > 0:
        for item in seq:
            if word.startswith(item):
                rest = word[len(item):]
                if valid_word(seq, rest):
                    return True
        return False
    else:
        return True