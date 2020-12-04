import re

s = open("input.txt", "r")

counter = 0

for i in s.read().split("\n\n"):
    require_field = {
        "byr:": False,
        "iyr:": False,
        "eyr:": False,
        "hgt:": False,
        "hcl:": False,
        "ecl:": False,
        "pid:": False,
    }
    person_data = i.replace("\n", " ").split(" ")
    for data in person_data:
        for field in require_field.keys():
            if data.startswith(field):
                if field == "byr:":
                    byr = int(data.split(":")[1])
                    if byr >= 1920 and byr <= 2002:
                        require_field[field] = True
                elif field == "iyr:":
                    iyr = int(data.split(":")[1])
                    if iyr >= 2010 and iyr <= 2020:
                        require_field[field] = True
                elif field == "eyr:":
                    eyr = int(data.split(":")[1])
                    if eyr >= 2020 and eyr <= 2030:
                        require_field[field] = True
                elif field == "hgt:":
                    if data.endswith("cm"):
                        hgt = int(data.split(":")[1].replace("cm", ""))
                        if hgt >= 150 and hgt <= 193:
                            require_field[field] = True
                    elif data.endswith("in"):
                        hgt = int(data.split(":")[1].replace("in", ""))
                        if hgt >= 59 and hgt <= 76:
                            require_field[field] = True
                elif field == "hcl:":
                    hcl = data.split(":")[1]
                    if len(hcl) == 7 and re.sub(r"[0-9a-f]", "", hcl) == "#":
                        require_field[field] = True
                elif field == "ecl:":
                    ecl = data.split(":")[1]
                    if ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        require_field[field] = True
                elif field == "pid:":
                    pid = data.split(":")[1]
                    if len(pid) == 9 and re.sub(r"[0-9]", "", pid) == "":
                        require_field[field] = True

    if all(require_field.values()):
        counter += 1


print(counter)