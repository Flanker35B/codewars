'''
5 kyu
Name: Word Search Grid

https://www.codewars.com//kata/58bcdf9a7288983803000042
Task: Create a program to solve a word search puzzle.

In word search puzzles you get a square of letters and have to find specific words in them.
'''


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle.split('\n')

    def in_grid(self, x, y):
        return 0 <= x < len(self.puzzle) and 0 <= y < len(self.puzzle[x])


    def search(self, word):
        for i, row in enumerate(self.puzzle):
            for j, v in enumerate(row):
                if v == word[0]:
                    for (dX, dY) in ((0, 1), (0, -1), (1, 0), (-1, 0), 
                                     (1, 1), (1, -1), (-1, 1), (-1, -1)):
                        o = [(i + (dX * index), j + (dY * index)) for index in range(len(word))]
                        if all(self.in_grid(x, y) for (x, y) in o):
                            if ''.join(self.puzzle[x][y] for (x, y) in o) == word:
                                return Point(j, i), Point(*o[-1][::-1])
        return None