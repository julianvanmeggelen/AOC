from __future__ import annotations

class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def intersect(self, other: Range) -> Range | None:
        bottom = max(self.min,other.min)
        top = min(self.max, other.max)
        if bottom<=top:
            return Range(bottom, top)
        else: 
            return None
        
    def bottom_difference(self, other: Range) -> list[Range | None]: 
        if other.min > self.min:
            return (Range(self.min, other.min-1))
        return None
    
    def top_difference(self, other: Range) -> list[Range | None]: 
        if other.max < self.max:
            return (Range(other.max+1, self.max))
        return None

    def offset(self, offset:int) -> Range:
        return Range(self.min+offset, self.max+offset)

    def __hash__(self) -> int:
        return hash((self.min, self.max))

    def __eq__(self, other: Range) -> bool:
        return self.min == other.min and self.max == other.max

    def __repr__(self) -> str:
        return f"<Range min={self.min} max={self.max}>"

if __name__ == "__main__":
    lines = open('input.txt').readlines()
    mapped = list(map(int, lines.pop(0).strip('seeds: ').split()))

    rranges = [Range(mapped[i], mapped[i]+mapped[i+1]-1) for i in range(0, len(mapped), 2)]
    print(rranges)
    
    new = []
    changed = set()
    for l, line in enumerate(lines):
        print("--"*10)
        print(line)
        if any((c.isdigit()) for c in line):
            dest_start, org_start, length = map(int,line.split())
            other = Range(org_start, org_start+length)
            offset = dest_start - org_start
            for i, rrange in enumerate(rranges):
                #print(i, rrange, other, offset)
                if rrange not in changed:
                    print(rrange, other)
                    if (isct:=rrange.intersect(other)) is not None:
                        #print('sss')
                        new.append(isct.offset(offset))
                        changed.add(rrange)
                        print('isct', isct)
                        #process remainders
                        if (bottom_diff:=rrange.bottom_difference(other)) is not None:
                            rranges.append(bottom_diff)
                            print('bottom diff', bottom_diff)
                        if (top_diff:=rrange.top_difference(other)) is not None:
                            rranges.append(top_diff)
                            print('top diff', top_diff)

        else:
            rranges = rranges + new #merge new mappings with remaining mappings
            rranges = [el for el in rranges if el not in changed]
            changed = set()
            new = []
            print(line)
            print("rranges", rranges)
print(min(el for row in rranges for el in (row.min,row.max)))


     

