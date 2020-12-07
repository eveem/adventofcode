s = open("input.txt", "r")

counter = 0

for i in s.read().split("\n\n"):
    counter += len(set(c for c in i.replace("\n", "")))

print(counter)
