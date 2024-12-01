
num = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
}

if __name__ == "__main__":
    res = 0
    for line in open('input.txt').readlines():
        line_digits, search_start= [], 0
        for search_start in range(0,len(line)):
            search_end = search_start
            for search_end in range(search_start,len(line)+1):
                if (substr:= line[search_start:search_end]) in num:
                    line_digits.append(substr)
        res += int(num[line_digits[0]]+num[line_digits[-1]])
    print(res)
    

