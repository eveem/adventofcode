s = open('input.txt', 'r')
r = 0

for i in s.readlines():
    i = i.replace('\n', '')
    x = [int(j) for j in i.split('x')]
    x.sort()
    # r += (2 * x[0] * x[1] + 2 * x[1] * x[2] + 2 * x[2] * x[0] + x[0] * x[1])
    r += (x[0] * x[1] * x[2] + x[0] + x[0] + x[1] + x[1])

print(r)
