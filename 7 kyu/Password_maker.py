'''
7 kyu
Name: Replace all items
https://www.codewars.com//kata/57ae18c6e298a7a6d5000c7a
Task: Write function replaceAll (Python: replace_all) that will replace all occurrences of an item with another.

Python / JavaScript: The function has to work for strings and lists.
'''

def replace_all(obj, find, replace):
    fl=0
    if isinstance(obj, str):
        obj=list(obj)
        fl=1
    for i,it in enumerate(obj):
        if it==find:
            obj[i]=replace
    if fl:
        obj=''.join(obj)
    return obj