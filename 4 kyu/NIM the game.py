'''
4 kyu
Name: NIM the game

https://www.codewars.com/kata/54120de842dff35232000195
Task: In this kata, you have to write an AI to play the straw picking game.

You have to encode an AI in a function choose_move (or chooseMove, or choose-move) that takes a board, represented as a 
list of positive integers, and returns

(pile_index, number_of_straws)
Which refers to an index of a pile on the board, and some none-zero number of straws to draw from that pile.

The test suite is written so that your AI is expected to play 50 games and win every game it plays.
'''

def choose_move(game_state):
    sg = 0
    for a in game_state:
        sg ^= a

    for i, a in enumerate(game_state):
        if a > a ^ sg:
            return [i, a - (a ^ sg)]