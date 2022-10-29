'''
7 kyu
Name: Sort an array by value and index
https://www.codewars.com//kata/58e0cb3634a3027180000040
Task: Sort an array by value and index
Your task is to sort an array of integer numbers by the product of the value and the index of the positions.

For sorting the index starts at 1, NOT at 0!
The sorting has to be ascending.
The array will never be null and will always contain numbers.
'''

def sort_by_value_and_index(arr):
    return [arr[1] for arr in sorted(enumerate(arr),key=lambda x:(x[0] + 1) * x[1])]