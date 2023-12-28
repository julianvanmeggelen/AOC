if __name__ == "__main__":
    lines = open('input.txt').readlines()
    nodes = [[*line] for line in lines]
    y = 0
    while not 'S' in nodes[y]:
        y+=1
    x = nodes[y].index('S')
    curr = (x*2,y*2)
    curr_node = ''
    dir = (0,-1)
    i = 0
    visited = [[0] * len(nodes[0]) * 2 for _ in range(len(nodes)*2)]
    while not curr_node == 'S':
        visited[curr[1]][curr[0]]=1
        i+=1
        if curr_node in ('L', '7'): dir = (dir[1], dir[0])
        if curr_node in ('J', 'F'): dir = (-1*dir[1], -1*dir[0])
        curr = curr[0]+dir[0], curr[1]+dir[1]
        visited[curr[1]][curr[0]]=1
        curr = curr[0]+dir[0], curr[1]+dir[1]
        curr_node = nodes[int(curr[1]/2)][int(curr[0]/2)]
    curr = (0,0)
    queue = [curr]
    while queue:
        curr = queue.pop()
        if not(curr[0] > len(visited[0])-1 or curr[1] > len(visited)-1 or curr[0] < 0 or curr[1] < 0 or visited[curr[1]][curr[0]] != 0):
            visited[curr[1]][curr[0]] = 1
            queue+= [(curr[0]+1, curr[1]), (curr[0]-1, curr[1]), (curr[0], curr[1]+1), (curr[0], curr[1]-1)]
    visited = [[max(row[i], row[i+1]) for i in range(0, len(row), 2)] for row in visited]
    visited = [[max(visited[i][j], visited[i+1][j]) for j in range(len(visited[0]))] for i in range(0, len(visited), 2)]
    print(len(visited) * len(visited[0]) - sum(sum(row) for row in visited))
    



    




  


    


     

