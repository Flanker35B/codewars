'''
4 kyu
Name: Golf [Code Golf]

https://www.codewars.com/kata/5e91c0f2b89d48002eee828b
Task:  You find yourself in a rectangular golf field like this one (ignore the borders):

+----------+
| **    ***|
|       ***|
|****##    |
|    **    |
|*        F|
+----------+
In these fields you can find empty spaces, bushes (*), walls (#) and a flag (F). You start from a position with 
coordinates (i, j) (row, column), with (0, 0) being at the top-left corner.

From the position you are on, you can hit the ball in a straight horizontal or vertical line, having it land on any empty space.

Your task
Write a function golf(field: List[str], i: int, j: int, hits: int) that returns True when it is possible for the ball to
 reach the flag in hits movements or less and False in any other case. We define a movement as a hit with the rules mentioned in the previous section.

The field argument will be given as a list of str and can be mutated, but it is not necessary to complete this task.

Golf 2
Again, you have a character limit to complete this task. In this case it's 200 characters or less, and written on one 
single line, but I might try to lower it depending on how you guys do ;D
'''


def golf(F, I, J, H, S=0, d=[1,3,5,7]): return all([H+1,I+1,I<len(F),J+1,J<len(F[0])])and'#'!=F[I][J]and(F[I][J]=='F'or any((golf(F,I-1+s%3,J-1+s//3,H-(s!=S),s)for s in d if'*'!=F[I][J]or s==S)))