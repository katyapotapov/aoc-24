from time import sleep
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

# print(unpacked_disk_map)

while list(set(unpacked_disk_map[-unpacked_disk_map.count("."):])) != ["."]:
    last_char = ""
    last_char_i = 0
    for i in range(len(unpacked_disk_map)-1, -1, -1):
        if unpacked_disk_map[i] == ".":
            continue
        last_char = unpacked_disk_map[i]
        last_char_i = i
        break
    # print(f"{last_char=}")
    # print(last_char_i)
    unpacked_disk_map[last_char_i] = "."
    first_empty_space = unpacked_disk_map.index(".")
    # print(first_empty_space)
    unpacked_disk_map[first_empty_space] = last_char
    # print(unpacked_disk_map)

chk = 0
for i, c in enumerate(unpacked_disk_map):
    if c == ".":
        continue
    chk += i * int(c)

print(chk)
