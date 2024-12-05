from collections import defaultdict

def read_input(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines

def escape(s):
    res = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i] == "\\":
            if s[i + 1] == '\"' or s[i + 1] == "\\":
                res += 1
                i += 2
            elif s[i + 1] == "x":
                res += 1
                i += 4
        else:
            res += 1
            i += 1

    return res

def encode(s):
    res = 0
    i = 0
    n = len(s)

    while i < n:
        if s[i] == "\"" or s[i] == "\\":
            res += 1
        res += 1
        i += 1
    
    return res

def first_star():
    # lines = read_input("small_input.txt")
    lines = read_input("input.txt")
    total = 0
    for line in lines:
        x = len(line)
        y = escape(line) - 2
        total += x - y
    print(f"first star result: {total}")

def second_star():
    # lines = read_input("small_input.txt")
    lines = read_input("input.txt")
    total = 0
    for line in lines:
        x = len(line)
        y = encode(line) + 2
        total += y - x
    print(f"second star result: {total}")

if __name__ == "__main__":
    first_star()
    second_star()