
from itertools import product


class Equation:
    def __init__(self, eq_list):
        tupple = eq_list.split(": ")
        self.result = int(tupple[0])
        self.values = list(map(int, (tupple[1].rstrip()).split(" ")
                               )
                           )
        self.operators = []

    def generate_operators(self):
        self.operators = generate_combinations(len(self.values) - 1)

    def check_equation(self):
        self.generate_operators()
        for operator_list in self.operators:
            if self.calc_result(operator_list) == self.result:
                return self.result
        return 0

    def calc_result(self, op_list):
        res = self.values[0]
        for i in range(1, len(self.values)):
            op = op_list[i-1]
            if op == '+':
                res += self.values[i]
            elif op == '*':
                res *= self.values[i]
            else:
                str_val = str(res) + str(self.values[i])
                # print(f"res {res}, str_val {str_val}, val {self.values[i]}")
                res = int(str_val)
        return res


def generate_combinations(n):
    chars = ['+', '*', '||']
    combinations = list(product(chars, repeat=n))
    return [list(combination) for combination in combinations]


with open("input.txt", 'r') as input_file:
    equations = 0
    for line in input_file:
        # print(line.split(": "))
        eq = Equation(line)
        equations += eq.check_equation()
    print(equations)
