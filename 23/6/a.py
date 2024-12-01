

import math


if __name__ == "__main__":
    lines = open('input.txt').readlines()
    times = map(int, lines[0].strip('Time:').strip('').split())
    distances = map(int, lines[1].strip('Distance:').strip('').split())
    res = []
    for time, distance in zip(times, distances):
        print(time,distance)
        n = 0
        for t in range(time):
            if (time-t)*t > distance:
                n+=1
        res.append(n)
    print(math.prod(res))
    


    


     

