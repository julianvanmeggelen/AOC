instrs = [int(el) for el in open('input.txt').readlines()[-1].split()[1].split(',')]
reg = [61156655, 0, 0]
instr_ptr = 0 
combo_op = lambda val: val if val <=3 else reg[val-4]
out = []
while instr_ptr < len(instrs)-1:
    instr, operand = instrs[instr_ptr], instrs[instr_ptr+1]
    print(instr_ptr, instr, operand)
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
            out.append(str(combo_op(operand) % 8))
        case 6:
            reg[1] =int(reg[0]/(2**combo_op(operand))) 
        case 7:
            reg[2] =int(reg[0]/(2**combo_op(operand))) 
    instr_ptr += 2

print(','.join(out))
