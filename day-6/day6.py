from collections import Counter

def part1():
    with open("input.csv") as f:
        qtd = 0
        file = f.read().split("\n\n")
        for line in file:
            line = line.replace("\n", "")
            
            s = set(line)
            qtd += len(s) 
        
        print(qtd)

def part2():
    with open("input.csv") as f:
        qtd = 0
        file = f.read().split("\n\n")
        for line in file:
            ap = []
            for l in line.split("\n"):
                for stuf in l:
                    ap.append(stuf)
            

            c = Counter(ap)
            commom_ids = [k for k, v in c.items() if v == len(line.split("\n"))]

            qtd += len(commom_ids)

        print(qtd)

if __name__ == "__main__":
    part1()
    part2()

