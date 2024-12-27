lines= [line.strip() for line in open('input.txt').readlines()]
patts = lines[0].split(', ')
from functools import cache

@cache
def design_possible(design: str) -> int:
    if len(design) == 0:
        return 1
    total = 0
    for patt in patts:
        if design.startswith(patt):
            total += design_possible(design[len(patt):])
    return total
print(sum(design_possible(design) for design in lines[2:]))
