ops = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT', '->']

s = open("input.txt", "r")
all_variable = {}

for i in s.read().splitlines():
    temp = i.split(' ')
    
    print(temp)