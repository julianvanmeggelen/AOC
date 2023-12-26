

import math


if __name__ == "__main__":
    lines = open('input.txt').readlines()
    time = int(''.join(lines[0].strip('Time:').strip('').split()))
    distance = int(''.join(lines[1].strip('Distance:').strip('').split()))
    print(time,distance)
    n = 0
    for t in range(time):
        if (time-t)*t > distance:
            n+=1
    print(n)
    


    


     

