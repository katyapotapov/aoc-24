
with open("input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

l = ls[0]

file = True
unpacked_disk_map = []
num_file = 0
for i in l:
    char_to_fill_in = ""
    if file:
        char_to_fill_in = str(num_file)
        num_file += 1
    else:
        char_to_fill_in = "."

    for _ in range(int(i)):
        unpacked_disk_map.append(char_to_fill_in)
    file = not file
#print("".join(unpacked_disk_map))
for file_id in range(num_file-1, -1, -1):
    last_char = str(file_id)
    #print(last_char)
    len_file = unpacked_disk_map.count(last_char) 
    #print("".join(unpacked_disk_map))
    
    first_empty_space = -1
    for i in range(len(unpacked_disk_map)-len_file):
        if set(unpacked_disk_map[i:i+len_file]) == set("."):
            first_empty_space = i
            break
    #print(first_empty_space)
    if first_empty_space != -1 and first_empty_space < unpacked_disk_map.index(last_char):
        unpacked_disk_map = [i if i != last_char else "." for i in unpacked_disk_map]
        for i in range(len_file):
            unpacked_disk_map[first_empty_space + i] = last_char
    #print("".join(unpacked_disk_map))


chk = 0
for i, c in enumerate(unpacked_disk_map):
    if c == ".":
        continue
    chk += i * int(c)

print(chk)


