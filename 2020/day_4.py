s = open("input.txt", "r")

require_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
require_field = [field + ":" for field in require_field]

counter = 0

for i in s.read().split("\n\n"):
    person_data = i.replace("\n", " ").split(" ")
    counter += (
        1
        if sum(
            1
            for field in require_field
            for data in person_data
            if data.startswith(field)
        )
        == 7
        else 0
    )

print(counter)