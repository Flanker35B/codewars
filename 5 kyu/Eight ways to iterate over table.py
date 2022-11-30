'''
5 kyu
Name: Eight ways to iterate over table

https://www.codewars.com//kata/5af5c18786d075cd5e00008b
Task: Since table has four corners, there are eight ways to iterate over its' elements ((by rows then by columns | by
 columns then by rows) * (top left to bottom right | top right to bottom left | bottom left to top right | bottom right to top left)).

Implement forward iterator that can be constucted with two directions as parameters that returns table items in specified 
order. (c++: implement begin(dir0,dir1) and end() functions, python: implement walk(dir0,dir1) function)
'''

DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1, 5)


class Table:
    def __init__(self, data):
        self.data = data
        self.ranges = {
            DIRECTION_UP: range(len(self.data) - 1, -1, -1),
            DIRECTION_DOWN: range(len(self.data)),
            DIRECTION_LEFT: range(len(self.data[0]) - 1, -1, -1),
            DIRECTION_RIGHT: range(len(self.data[0])),
        }

    def dir(self, direc):
        match direc:
            case 1:
                return range(self.width)
            case 2:
                return range(self.width - 1, -1, -1)
            case 3:
                return range(self.height)
            case 4:
                return range(self.height - 1, -1, -1)

    def walk(self, dir0, dir1):
        for y in self.ranges[dir1]:
            for x in self.ranges[dir0]:
                yield self.data[x][y] if dir1 % 2 == 0 else self.data[y][x]