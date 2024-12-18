import re
pattern = r".*X([+-=]\w+),\s*Y([+-=]\w+)"


class Computer:
    def __init__(self):
        self.reg_a = 0
        self.reg_b = 0
        self.reg_c = 0
        self.ip = 0
        self.instructions = []
        self.output = []

    def get_combo_value(self, op_code):
        if op_code >= 0 and op_code <= 3:
            return op_code
        elif op_code == 4:
            return self.reg_a
        elif op_code == 5:
            return self.reg_b
        elif op_code == 6:
            return self.reg_c
        else:
            assert False, "never look up the combo value of op code 7"

    def execute_instr(self, op_code, operand):
        # print(f"opcode {op_code}, operand {operand}")
        if op_code == 0:
            numerator = self.reg_a
            denominator = 2 ** self.get_combo_value(operand)
            self.reg_a = numerator // denominator
        elif op_code == 1:
            self.reg_b = self.reg_b ^ operand
        elif op_code == 2:
            self.reg_b = self.get_combo_value(operand) % 8
        elif op_code == 3:
            if self.reg_a != 0:
                self.ip = operand - 2
        elif op_code == 4:
            self.reg_b = self.reg_b ^ self.reg_c
        elif op_code == 5:
            self.output.append(self.get_combo_value(operand) % 8)
        elif op_code == 6:
            numerator = self.reg_a
            denominator = 2 ** self.get_combo_value(operand)
            self.reg_b = numerator // denominator
        elif op_code == 7:
            numerator = self.reg_a
            denominator = 2 ** self.get_combo_value(operand)
            self.reg_c = numerator // denominator

    def interpret(self, a, b, c, instr):
        self.reg_a = a
        self.reg_b = b
        self.reg_c = c
        self.ip = 0
        while self.ip < len(instr):
            self.execute_instr(instr[self.ip], instr[self.ip + 1])
            self.ip += 2
        ouput_str = list(map(str, self.output))
        return ",".join(ouput_str)


reg_a_small = 117440
# reg_a_small = 2024
reg_b_small = 0
reg_c_small = 0

reg_a = 46187030
reg_b = 0
reg_c = 0


with open("input.txt", 'r') as input_file:
    input = input_file.read()

    instr = list(map(int, input.rstrip().split(",")))
    counter = -1
    programlen = len(instr)
    output_r = "2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0".split(",")
    i1 = 10
    i2 = 11
    while True:
        # reg_a = 8 ** (15) + 4096 * 4096 * 32 * counter
        # reg_a = 105827994173440 - 32 * 4096 * counter
        reg_a = 8 ** (16) - counter * 100000
        print(reg_a)
        computer = Computer()
        output = computer.interpret(reg_a, 0, 0, instr)
        print(f"{output} len: {len(output.split(","))}")
        r = output.split(",")
        if r[i1] == output_r[i1] and r[i2] == output_r[i2]:
            break
        if output == "2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0":
            print(f"reg_a = {reg_a}")
            break
        counter += 1
    # computer.interpret(reg_a_small, 0, 0, instr)
