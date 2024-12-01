import math
if __name__ == "__main__":
    lines = open('input.txt').readlines()
    nodes = [[*line] for line in lines]
    y = 0
    while not 'S' in nodes[y]:
        y+=1
    x = nodes[y].index('S')

    curr = (x,y)
    curr_node = ''
    dir = (0,-1)
    i = 0
    while not curr_node == 'S':
        i+=1
        if curr_node in ('L', '7'): dir = (dir[1], dir[0])
        if curr_node in ('J', 'F'): dir = (-1*dir[1], -1*dir[0])
        curr = curr[0]+dir[0], curr[1]+dir[1]
        curr_node = nodes[curr[1]][curr[0]]
    print(math.floor(i/2))



    




  


    


     

