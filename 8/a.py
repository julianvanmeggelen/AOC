
if __name__ == "__main__":
    lines = open('input.txt').readlines()
    directions = [*lines[0].strip()]
    print(directions)
    nodes = {}
    for line in lines[2:]:
        k, lr = line.split(' = ')
        l,r = lr.strip(')\n').strip('(').split(', ')
        nodes[k] = (l,r)
    print(nodes)

    curr = 'AAA'

    n_steps = 0
    while not curr == 'ZZZ':
        for direction in directions:
            print(curr, direction)
            curr = nodes[curr][0] if direction == 'L' else nodes[curr][1] 
            n_steps+=1
    print(n_steps)
  


    


     

