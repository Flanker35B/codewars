'''
7 kyu
Name: Alphabet war
https://www.codewars.com//kata/59377c53e66267c8f6000027
Task: Write a function that accepts fight string consists of only small letters and return who wins the fight.
 When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return 
 Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1
The other letters don't have power and are only victims.
'''

def alphabet_war(fight):
    lst='wpbs'
    rst='mqdz'
    lres=0
    rres=0
    dt={'s': 1,'z': 1, 'b': 2,'d': 2,'p': 3,'q': 3,'w': 4,'m': 4}
    for i in range(0,len(fight)):
        if fight[i] in lst:
            lres+=dt[fight[i]]
        elif fight[i] in rst:
            rres+=dt[fight[i]]
        else:
            continue
    if rres>lres:
        return "Right side wins!"
    elif lres>rres:
        return "Left side wins!"
    else:
        return "Let's fight again!"