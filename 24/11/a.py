line = [int(el) for el in open('input.txt').readline().strip().split()]

mem={}
def split_num(el:int, times:int) -> int:
    if (el, times) in mem: 
        return mem[(el,times)]

    if times == 0:
        return 1
    if el == 0:
        ret = split_num(1, times-1)
    elif (len_el_str:=len(el_str:=str(el))) %2 == 0:
        ret =  split_num(int(el_str[:(split:=int(len_el_str/2))]), times-1) + split_num(int(el_str[split:]), times-1)
    else:
        ret = split_num(2024*el, times-1)

    mem[(el, times)] = ret
    return ret
    
total = 0
for el in line:
    total += split_num(el, 75)
print(total)
        
