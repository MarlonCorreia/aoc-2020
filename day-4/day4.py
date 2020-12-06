import re

obligatory = ["byr", "iyr", "eyr", "hgt", "hcl" , "ecl", "pid"]

def part1(file):
    qtd = 0
    for key in file:
        qtd += set(key).issuperset(set(obligatory))
    return qtd

def part2(file):
    qtd = 0 
    for key in file:
        if set(key).issuperset(set(obligatory)):
            if len(key["pid"]) == 9:
                if key["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', key["hcl"]):
                        if ("cm" in key["hgt"] and 193 >= int(key["hgt"].strip("cm")) >= 150) or ("in" in key["hgt"] and 76 >= int(key["hgt"].strip("in")) >= 59):
                            if 2030 >= int(key["eyr"]) >= 2020:
                                if 2020 >= int(key["iyr"]) >= 2010:
                                    if 2002 >= int(key["byr"]) >= 1920:
                                        qtd += 1                            
    return qtd



if __name__ == "__main__":
    with open("input.csv") as f:
        file = f.read().split("\n\n")

        for idx, line in enumerate(file):
            line = line.split()
            dicio = {}

            for elem in line:
                elem = elem.split(":")
                dicio[elem[0]] = elem[1]
            file[idx] = dicio

    print(part1(file))
    print(part2(file))