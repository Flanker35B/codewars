'''
6 kyu
Name: Kingdoms Ep1: Jousting
https://www.codewars.com//kata/6138ee916cb50f00227648d9
Task: The King organizes the jousting. You are a young human lady and your fiancé is an ogre. Today is his anniversary 
and he would love to visit the tournament, but it's forbidden for ogres to visit the Kingdom. So you decided to go there,
 to paint the exact moments of clash of cavalry and to present these paintings to your beloved.

You are given the array / tuple (listField) of two strings of equal length. Each the string contains "$->" and "<-P"
(knight with lance) respectively. The knights move towards each other and they can only take simultaneous steps of length 
vKnightLeft and vKnightRight. When the index of ">" is equal or more than the index of "<", return the array / tuple 
representing the knights' positions.
'''

def joust(list_field: tuple, v_knight_left: int, v_knight_right: int) -> tuple:
    if v_knight_left==v_knight_right==0:
        return list_field
    else:
        lp=2
        rp=len(list_field[0])-3
        while lp<rp:
            lp+=v_knight_left
            rp-=v_knight_right
        s=''
        for i in range(lp-2):
            s+=' '
        s+='$->'   
        for i in range(lp,len(list_field[0])-1):
            s+=' '
        r=''
        for i in range(rp):
            r+=' '
        r+='<-P'   
        for i in range(rp+3,len(list_field[0])):
            r+=' '
        return (s,r)