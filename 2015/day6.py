s = open("input.txt", "r")

m = []
for i in range(1000):
    m.append([0 for j in range(1000)])

def switch(command, value):
    if command == 'on':
        return 1
    elif command == 'off':
        if value - 1 >= 0:
            return -1
        else:
            return 0
    elif command == 'toggle':
        return 2

for i in s.read().splitlines():
    temp = i.split(",")
    command = temp[0].split(" ")[-2]
    x1 = int(temp[0].split(" ")[-1])
    y1 = int(temp[1].split(" ")[0])
    x2 = int(temp[1].split(" ")[-1])
    y2 = int(temp[2].split(" ")[0])

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            m[x][y] += switch(command, m[x][y])

counter = 0

for i in range(1000):
    for j in range(1000):
        counter += m[i][j]

print(counter)
