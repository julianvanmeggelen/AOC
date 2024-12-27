instrs = tuple(int(el) for el in open('input.txt').readlines()[-1].split()[1].split(','))
A = 0
for i in reversed(range(len(instrs))):
    A <<= 3
    while True:
        print(A)
        reg = [A, 0, 0]
        instr_ptr = 0 
        combo_op = lambda val: val if val <=3 else reg[val-4]
        out = []
        while instr_ptr < len(instrs)-1:
            instr, operand = instrs[instr_ptr], instrs[instr_ptr+1]
            match instr:
                case 0:
                    reg[0] =int(reg[0]/(2**combo_op(operand))) 
                case 1:
                    reg[1] = reg[1] ^ operand
                case 2: 
                    reg[1] = combo_op(operand) % 8
                case 3:
                    if reg[0] > 0:
                        instr_ptr = operand - 2
                case 4:
                    reg[1] = reg[1] ^ reg[2]
                case 5:
                    out.append(combo_op(operand) % 8)
                case 6:
                    reg[1] =int(reg[0]/(2**combo_op(operand))) 
                case 7:
                    reg[2] =int(reg[0]/(2**combo_op(operand))) 
            instr_ptr += 2
        print(out)
        if tuple(out) == instrs[i:]:
            print(i)
            break
        A += 1
