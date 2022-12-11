'''
4 kyu
Name: Snail

https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
Task:  Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
'''

def snail(array):
    res = []
    if array and array[0]:
        size = len(array)
        for n in range((size + 1) // 2):
            for x in range(n, size - n):
                res.append(array[n][x])
            for y in range(1 + n, size - n):
                res.append(array[y][-1 - n])
            for x in range(2 + n, size - n + 1):
                res.append(array[-1 - n][-x])
            for y in range(2 + n, size - n):
                res.append(array[-y][n])
    return res