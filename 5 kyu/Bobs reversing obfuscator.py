'''
5 kyu
Name: Bob's reversing obfuscator

https://www.codewars.com//kata/559ee79ab98119dd0100001d
Task: Carol's boss Bob thinks he is very smart. He says he made an app which renders messages unreadable without changing
 any letters, only by adding some new ones, while preserving message integrity (i. e. the original message can still be retrieved).

He gave some limited access to his app to Carol to challenge her, and hinted that if Carol cannot crack this simple task, she might be fired.

Carol was trying to crack this code herself, but got too tired, so she came to you for help. However, she succeeded to hack
 Bob's app and found a data field called 'marker'. She thinks it can be helpful for cracking Bob's app.
'''

def decoder(s, m):
    narez = s.split(m)
    start = ''
    end = ''
    for i in range(len(narez)):
        if i % 2 == 0:
            start += narez[i]
        else:
            end += narez[i]
    return start + end[::-1]