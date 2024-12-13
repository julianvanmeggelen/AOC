

def find_space_for_file(disk, length, max_end_index):
    run_start = None
    for i in range(max_end_index):
        if disk[i] == '.':
            if run_start is None:
                run_start = i
        else:
            if run_start is not None:
                run_len = i - run_start
                if run_len >= length:
                    return run_start
                run_start = None
    if run_start is not None:
        run_len = max_end_index - run_start
        if run_len >= length:
            return run_start

    return None


line = open('input.txt').readline().strip()
disk = []
file_id = 0
for i, ch in enumerate(line):
    length = int(ch)
    if i % 2 == 0:
        disk.extend(str(file_id) for _ in range(length))
    else:
        disk.extend('.' for _ in range(length))
        file_id += 1

file_ids = set()
for block in disk:
    if block != '.':
        file_ids.add(int(block))
file_ids = sorted(file_ids, reverse=True)

for fid in file_ids:
    str_fid = str(fid)
    start = None
    end = None
    for i, block in enumerate(disk):
        if block == str_fid:
            if start is None:
                start = i
            end = i
    if start is None:
        continue
    length = (end - start + 1)
    file_blocks = start, end, length
    start, end, length = file_blocks
    
    target_start = find_space_for_file(disk, length, start)

    if target_start is None:
        continue

    
    file_id_char = str(fid)
    for i in range(start, end + 1):
        disk[i] = '.'
    for i in range(length):
        disk[target_start + i] = file_id_char

checksum = 0
for i, block in enumerate(disk):
    if block != '.':
        fid = int(block)
        checksum += i * fid

print(checksum)