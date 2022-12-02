'''
5 kyu
Name: Dating with hypergamy

https://www.codewars.com//kata/5f304fb8785c540016b9a97b
Task: A number of single men and women are locked together for a longer while in a villa or on an island, for the sake of 
a TV show. Because they spend quite some time together, all of them seek a partner to date. They are all shallow people, 
and they only care about looks, aka physical attractiveness when it comes to dating. Looks levels range from 1 to 10.
You'll be given a list of looks levels representing the men, and another list representing the women. Return a list of 
the looks levels of the men who stay alone, sorted from hideous to handsome.
'''


def guys_alone_from_group(men, women):
    if not men: return []
    if not women: return sorted(men)

    x = min(women)
    alone, b = [], []
    for i in men:
        if i < x:
            alone.append(i)
        else:
            b.append(i)

    b = [(i, 2 if i >= 8 else 1) for i in b]

    for w in sorted(women, reverse=True):
        b = sorted(b, key=lambda x: (x[0], x[1]), reverse=True)
        for j in range(len(b)):
            m = b[j][0]
            if m >= w + 2 or (m >= 8 and w <= m):
                if b[j][1] > 1:
                    b[j] = (b[j][0], 1)
                else:
                    b = b[:j] + b[j + 1:]
                break

    return sorted(alone + [i[0] for i in b if (i[0] >= 8 and i[1] == 2) or i[0] < 8])
