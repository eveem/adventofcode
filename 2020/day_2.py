s = open("input.txt", "r")


def input_format(i):
    temp = i.split(" ")
    lowest = int(temp[0].split("-")[0])
    highest = int(temp[0].split("-")[1])

    indicator = temp[1][0]
    password = temp[2]

    return lowest, highest, indicator, password


def path_1_solution(lowest, highest, indicator, password):
    counter = password.count(indicator)

    if counter >= lowest and counter <= highest:
        return 1
    return 0


def path_2_solution(lowest, highest, indicator, password):
    if (password[lowest - 1] == indicator) ^ (password[highest - 1] == indicator):
        return 1
    return 0


result_1 = 0
result_2 = 0

for i in s.read().splitlines():
    lowest, highest, indicator, password = input_format(i)
    result_1 += path_1_solution(lowest, highest, indicator, password)
    result_2 += path_2_solution(lowest, highest, indicator, password)

print(result_1)
print(result_2)