import math
if __name__ == "__main__":
    lines = open('input.txt').readlines()
    res = 0.0
    for line in lines:
        pos, cont = line.split()
        pos = [len(_) for _ in pos.split('.') if len(_)>0]
        cont = [int(_) for _ in  cont.split(',')]
        print(cont,pos)
        print(math.prod(math.comb(a,b) for a,b in zip(pos,cont)))
        res += math.prod(math.comb(a,b) for a,b in zip(pos,cont))
    print(res)
        
   

   






    


     

