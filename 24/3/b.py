i = 0 
line = open('input.txt').read()
total = 0
enabled = True
while i<len(line):
    if line[i:].startswith('do()'):
        enabled = True
    if line[i:].startswith("don't()"):
        enabled = False
    if line[i:].startswith('mul(') and enabled:
        i+=4
        j = i
        while line[j].isdigit():
            j+=1
        n1 = int(line[i:j])
        if line[j] == ',':
            j+=1
            k=j
            while line[k].isdigit():
                k+=1
            n2 = int(line[j:k])
            if line[k] == ')':
                total+=n1*n2
    i+=1
print(total)
