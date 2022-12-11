'''
4 kyu
Name: Unflatten a list (Harder than easy)

https://www.codewars.com/kata/57e5aa1d7fbcc988800001ae
Task:  - You have to do several runs. The depth is the number of runs, you have to do.
- In every run you have to switch the direction. First run from left, next run from right. Next left...
Every run has these rules:
- You start at the first number (from the direction).
- Take for every number x the remainder of the division by the number of still available elements (from 
  this position!) to have the number for the next decision.
- If the remainder-value is smaller than 3, take this number x (NOT the remainder-Value) direct
  for the new array and continue with the next number.
- If the remainder-value (e.g. 3) is greater than 2, take the next remainder-value-number (e.g. 3)
  elements/numbers (inclusive the number x, NOT the remainder-value) as a sub-array in the new array.
  Continue with the next number/element AFTER this taken elements/numbers.
- Every sub-array in the array is independent and is only one element for the progress on the array. 
  For every sub-array you have to follow the same rules for unflatten it.
  The direction is always the same as the actual run.
'''


def unflatten(flat_array, depth, direction = 1):
    if depth == 0:
        return flat_array
    ind = 0
    array = []
    flat_array = flat_array[::direction]
    while ind < len(flat_array):
        nleft = len(flat_array) - ind
        elem = flat_array[ind]
        if type(flat_array[ind]) is list:
            array.append(unflatten(flat_array[ind], 1, direction))
            ind += 1
        elif elem % nleft < 3:
            array.append(elem)
            ind += 1
        else:
            array.append(flat_array[ind:ind + elem % nleft][::direction])
            ind += elem % nleft
    return unflatten(array[::direction], depth-1, -direction)