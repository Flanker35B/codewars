'''
5 kyu
Name: Binary relation optimization

https://www.codewars.com//kata/603928e6277a4e002bb33d5a
Task: Given a binary relation, you have to perform an optimization on it. In this case, find a list of options which are
 collectively better than all the other options. Such options satisfy the following 2 criteria:

all the options included in the result are not directly related to each other
for each option not included in the result there must be at least one better option which is included in the result
'''

def optimize(adj_matrix):
    options = [i for i in range(len(adj_matrix))]
    results = []
    n = len(options)
    while n > 0:
        for i in options:
            sum_i = 0
            for j in options:
                sum_i += adj_matrix[j][i]
            if sum_i == 0:
                test_i = True
                for j in results:
                    if adj_matrix[j][i] == 1:
                        test_i = False
                if test_i:
                    results.append(i)
                options.remove(i)
                n -= 1
    results.sort()       
    return results