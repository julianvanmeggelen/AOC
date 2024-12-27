lines= [line.strip() for line in open('input.txt').readlines()]
patts = lines[0].split(', ')

def design_possible(design: str):
    if len(design) == 0:
        return True
    
    for patt in patts:
        if design.startswith(patt):
            if design_possible(design[len(patt):]):
                return True
    return False

print(sum(design_possible(design) for design in lines[2:]))
