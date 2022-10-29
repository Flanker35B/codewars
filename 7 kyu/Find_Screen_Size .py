'''
7 kyu
Name: Tetris Series #1 — Scoring System
https://www.codewars.com//kata/5da9af1142d7910001815d32
Task: The scoring formula is built on the idea that more difficult line clears should be awarded more points. For 
example, a single line clear is worth 40 points, clearing four lines at once (known as a Tetris) is worth 1200.

A level multiplier is also used. The game starts at level 0. The level increases every ten lines you clear. Note that 
after increasing the level, the total number of cleared lines is not reset.

Calculate the final score of the game using original Nintendo scoring system
'''


def get_score(arr):
    score = 0
    lvl = 1
    s = 0
    for i in arr:
        s += i
        match i:
            case 1:
                score += 40 * lvl
            case 2:
                score += 100 * lvl
            case 3:
                score += 300 * lvl
            case 4:
                score += 1200 * lvl
        if s >= 10:
            lvl += 1
            s -= 10

    return score
