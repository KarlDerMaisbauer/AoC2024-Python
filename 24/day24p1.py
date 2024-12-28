from collections import deque
import re


class Option:
    def __init__(self, value=None):
        self.value = value

    def is_some(self):
        return self.value != None

    def unwrap(self):
        return self.value

    @staticmethod
    def none():
        return Option()

    @staticmethod
    def some(val):
        return Option(val)

    def __str__(self):
        if self.is_some():
            return f"Some({self.value})"
        else:
            return " None()"


class Solver:
    def __init__(self):
        self.vars = {}
        self.formulas = deque([])

    def add_var(self, name, val=Option.none()):
        if not name in self.vars:
            # print(f"add new key {name}")
            self.vars[name] = val

    def add_formula(self, var1, var2, op, res_var):
        self.formulas.append((var1, var2, op, res_var))

    def solve(self):
        while len(self.formulas) != 0:
            # print("#######################")
            formula = self.formulas.pop()
            # print(f"curr formula {formula}")
            if not self.vars[formula[0]].is_some():
                # print("put it back")
                self.formulas.appendleft(formula)
            elif not self.vars[formula[1]].is_some():
                # print("put it back2")
                self.formulas.appendleft(formula)
            else:
                val1 = self.vars[formula[0]].unwrap()
                val2 = self.vars[formula[1]].unwrap()
                op = formula[2]
                res_name = formula[3]
                # print(f"solving {formula}")
                # print(f"var1 {val1}({formula[0]}) {
                # op}({formula[1]}) var2 {val2}")
                if op == "AND":
                    self.vars[res_name] = Option.some(val1 and val2)
                elif op == "XOR":
                    self.vars[res_name] = Option.some(val1 ^ val2)
                else:
                    self.vars[res_name] = Option.some(val1 or val2)
            # print(self.formulas)
        result_keys = [key for key in self.vars if key.startswith(
            'z') and key[1:].isdigit()]
        result_keys.sort(reverse=True)
        # for key, val in self.vars.items():
        # print(f"{key}: {val}")
        res_val_str_arr = []
        for key in result_keys:
            res_val_str_arr.append(str(int(self.vars[key].unwrap())))

        print(int("".join(res_val_str_arr), 2))


with open("input.txt", 'r') as input_file:
    solver = Solver()
    iter = iter(input_file)
    pattern = r' (AND|XOR|OR) '
    for line in iter:
        line_str = line.rstrip()
        if line_str == "":
            break
        var_parts = line_str.split(": ")
        solver.add_var(var_parts[0], Option.some(bool(int(var_parts[1]))))
    for line in iter:
        line_str = line.rstrip()
        if line_str == "":
            break
        first_split = line_str.split(" -> ")
        res_var = first_split[1]
        solver.add_var(res_var)
        formula_parts = re.split(pattern, first_split[0])

        solver.add_formula(
            formula_parts[0], formula_parts[2], formula_parts[1], res_var)
    solver.solve()
    # print("##############################")
    # for (key, var) in solver.vars.items():
    #     print(f"{key}, {var}")
    # print("##############################")
