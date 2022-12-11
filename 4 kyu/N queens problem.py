'''
4 kyu
Name: N queens problem (with no mandatory queen position)

https://www.codewars.com/kata/52cdc1b015db27c484000031
Task:  This is a classic needing (almost) no further introduction.

Given a N x N chess board, place N queens on it so none can attack another: I.e. no other queens can be found horizontally,
 vertically or diagonally to the current.

On the board below, no further queens can be positioned.

+-+-+
|Q| |
+-+-+
| | |
+-+-+
'''


def nQueen(n):
    if n==2 or n==3: return []
    r, odds, evens = n%6, list(range(1,n,2)), list(range(0,n,2))
    if r==2:
        evens[:2] = evens[:2][::-1]
        evens.append(evens.pop(2))
    if r==3:
        odds.append(odds.pop(0))
        evens.extend(evens[:2])
        del evens[:2]
    return odds+evens