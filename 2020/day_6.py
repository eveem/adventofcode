s = open("input.txt", "r")

counter = 0

for i in s.read().split("\n\n"):
    # counter += len(set(c for c in i.replace("\n", "")))

    temp = {}
    checker = len(i.split("\n"))
    for c in i.replace("\n", ""):
        if c not in temp:
            temp[c] = 1
        else:
            temp[c] += 1

    counter += sum(1 for x in temp.values() if x == checker)

print(counter)
