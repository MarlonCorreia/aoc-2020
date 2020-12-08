
dic = {}
my_bag = "shiny gold"

with open("input.csv") as f:
    for line in f:
        if "no other" in line:
            l = line.split("contain")[0].split(",")[0].rsplit()
            dic[l[0] + " " + l[1]] = set({})
            continue

        l = line.split("contain")[0].split(",")[0].rsplit()
        dic[l[0] + " " + l[1]] = set({})

        for x in line.split("contain")[1].split(","):
            dic[l[0] + " " + l[1]].add(x.strip().split()[1] + " " + x.strip().split()[2])
        




def find_qtd(group, query):
    found = []
    for k in group.keys():
        if query in dic[k]:
            found.append(k)
            found.extend(find_qtd(group, k))
    return found
            



res = find_qtd(dic, my_bag)
print(len(set(res)))