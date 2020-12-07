m = 0
a = []

s = open("input.txt", "r")

for line in s.read().splitlines():
    rows = line[0:7]
    cols = line[7:]

    x1 = 0
    x2 = 127

    y1 = 0
    y2 = 7

    for i in rows:
        if i == "F":
            x2 = (x1 + x2) // 2
        elif i == "B":
            x1 = (x1 + x2) // 2 + 1

    for i in cols:
        if i == "L":
            y2 = (y1 + y2) // 2
        elif i == "R":
            y1 = (y1 + y2) // 2 + 1

    r = x1 * 8 + y1
    if r > m:
        m = r
    a.append(r)

a.sort()
prev = a[0]
for i in a[1:]:
    if prev + 1 != i:
        print(prev, i)
    prev = i