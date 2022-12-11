'''
4 kyu
Name: Data mining #2

https://www.codewars.com/kata/591748b3f014a2593d0000d9
Task:  Your task is to build a model1 which can predict y-coordinate.
You can pass tests if predicted y-coordinates are inside error margin.


You will receive train set which should be used to build a model.
After you build a model tests will call function predict and pass x to it.


Error is going to be calculated with RMSE.


Side note: Points in test cases are from different polynomials (up to 5th degree).
'''


class Datamining:

    def __init__(self, train_set):
        train_set = list(set(train_set))[:6]
        self.interpretation = self.lagrange_interp(train_set)

    def lagrange_interp(self, train_set):
        interp = ''
        for i, (xi, yi) in enumerate(train_set):
            for j, (xj, _) in enumerate(train_set):
                if i != j:
                    interp += f"(x-{xj})/{(xi - xj)}*"
            interp += f"{yi}+"
        return interp[:-1]

    def predict(self, x):
        return eval(self.interpretation, {'x': x})