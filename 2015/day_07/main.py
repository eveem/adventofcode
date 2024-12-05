from collections import defaultdict

def read_input(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

def not_op(s):
    res = ""
    for c in s:
        if c == "1":
            res += "0"
        if c == "0":
            res += "1"
    return res

def and_op(x, y):
    res = ""
    for a, b in zip(x, y):
        if a == b:
            res += a
        else:
            res += "0"
    return res

def or_op(x, y):
    res = ""
    for a, b in zip(x, y):
        if a == "1" or b == "1":
            res += "1"
        else:
            res += "0"
    return res

def lshift_op(s, n):
    return s[n:] + ("0" * n)

def rshift_op(s, n):
    return ("0" * n) + s[:-n] 

def extract(lines):
    variables = defaultdict(int)
    i = 0
    while i != len(lines):
        for s in lines:
            ops = s.split(" ")
            if len(ops) == 3 and ops[1] == "->":
                if ops[0].isdigit():
                    variables[ops[2]] = bin(int(ops[0]))[2:].zfill(16)
                elif ops[0] in variables:
                    variables[ops[2]] = variables[ops[0]]
            elif ops[0] == "NOT":
                if ops[1] in variables:
                    variables[ops[3]] = not_op(variables[ops[1]])
            elif ops[1] == "AND":
                if ops[0] in variables and ops[2] in variables:
                    variables[ops[4]] = and_op(variables[ops[0]], variables[ops[2]])
                elif ops[0] in variables and ops[2].isdigit():
                    variables[ops[4]] = and_op(variables[ops[0]], bin(int(ops[2]))[2:].zfill(16))
                elif ops[0].isdigit() and ops[2] in variables:
                    variables[ops[4]] = and_op(bin(int(ops[0]))[2:].zfill(16), variables[ops[2]])
            elif ops[1] == "OR":
                if ops[0] in variables and ops[2] in variables:
                    variables[ops[4]] = or_op(variables[ops[0]], variables[ops[2]])
                elif ops[0] in variables and ops[2].isdigit():
                    variables[ops[4]] = or_op(variables[ops[0]], bin(int(ops[2]))[2:].zfill(16))
                elif ops[0].isdigit() and ops[2] in variables:
                    variables[ops[4]] = or_op(bin(int(ops[0]))[2:].zfill(16), variables[ops[2]])
            elif ops[1] == "LSHIFT":
                if ops[0] in variables:
                    variables[ops[4]] = lshift_op(variables[ops[0]], int(ops[2]))
            elif ops[1] == "RSHIFT":
                if ops[0] in variables:
                    variables[ops[4]] = rshift_op(variables[ops[0]], int(ops[2]))
        i += 1

    for k, v in variables.items():
        variables[k] = int(v, 2)
    return variables["a"]
        
# extract assign first
# then NOT
# AND
# OR

def first_star():
    # lines = read_input("small_input.txt")
    lines = read_input("input.txt")
    print(f"first star result: {extract(lines)}")

def second_star():
    lines = read_input("input.txt")
    print(f"second star result: {extract(lines)}")

if __name__ == "__main__":
    first_star()
    second_star()