
import math
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

    starting_nodes = [k for k in nodes if k[-1] == 'A']
    all_n_steps = []
    for node in starting_nodes:
        curr = node
        n_steps = 0
        while not curr[-1] == 'Z':
            for direction in directions:
                #print(curr)
                i = 0 if direction == 'L' else 0
                curr = nodes[curr][0] if direction == 'L' else nodes[curr][1] 
                n_steps+=1
        all_n_steps.append(n_steps)
    print(math.lcm(*all_n_steps))
  


    


     

