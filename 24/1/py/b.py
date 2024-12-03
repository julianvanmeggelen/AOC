lines = open("input.txt").readlines()
left = [int(line.split()[0]) for line in lines]
right = [int(line.split()[1]) for line in lines]

counts_dict = {}
for el in right: 
    if el not in counts_dict: counts_dict[el] = 0
    counts_dict[el]+=1
print(sum(el * (counts_dict[el] if el in counts_dict else 0) for el in left))