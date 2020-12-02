


def part1():
    resp = 0
    with open("input.csv") as f:
        for line in f.readlines():
            general = line.split()
            letter = general[1].split(":")[0]
            count = general[0].split("-")
            passw = general[2]
            
        

            if int(count[0]) <= passw.count(letter) and int(count[1]) >= passw.count(letter):
                resp += 1

    print(resp)

def part2():
    resp = 0
    with open("input.csv") as f:
            for line in f.readlines():
                general = line.split()
                letter = general[1].split(":")[0]
                count = general[0].split("-")
                passw = list(general[2])

                
                if (passw[int(count[0]) - 1] == letter and passw[int(count[1]) - 1] != letter) or (passw[int(count[0]) - 1] != letter and passw[int(count[1]) - 1] == letter):
                    resp += 1

            print(resp)


if __name__ == "__main__":
    part1()
    part2()