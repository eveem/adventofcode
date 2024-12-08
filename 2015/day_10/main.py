def read_input(filename):
    with open(filename, "r") as file:
        for line in file:
            return line.strip()

def group(s):
    res = []
    curr = 1
    prev = s[0]
    
    for c in s[1:]:
        if c != prev:
            res.append((curr, prev))
            curr = 0
        prev = c
        curr += 1
    
    res.append((curr, prev))
    
    return res

def transform(grouped):
    res = ""
    
    for x, y in grouped:
        res += str(x) + y
    
    return res

def first_star():
    # s = read_input("small_input.txt")
    s = read_input("input.txt")

    for _ in range(40):
        grouped = group(s)
        s = transform(grouped)
    
    print(f"first star result: {len(s)}")

def second_star():
    # s = read_input("small_input.txt")
    s = read_input("input.txt")

    for _ in range(50):
        grouped = group(s)
        s = transform(grouped)
    
    print(f"second star result: {len(s)}")

if __name__ == "__main__":
    first_star()
    second_star()