s = open("input.txt", "r")

m = []

for i, j in enumerate(s.read().splitlines()):
    m.append(j)

ROW = len(m)
COL = len(m[0])


def process(right, down):
    x = 0
    y = 0
    counter = 0
    while y < ROW:
        if m[y][x] == "#":
            counter += 1

        y += down
        x += right

        if x >= COL:
            x = x - COL

    return counter


print(process(1, 1) * process(3, 1) * process(5, 1) * process(7, 1) * process(1, 2))