with open("input_full.txt") as f:
    ls = f.readlines()

# horizontal + hor backward
# this one's correct
total_words = 0
for l in ls:
    total_words += l.count("XMAS")
    total_words += l.count("SAMX")

# vertical
# also correct
vert_lines = []
for j in range(len(l)):
    line = ""
    for i in range(len(ls)):
        line += ls[i][j]
    vert_lines.append(line)
for l in vert_lines:
    total_words += l.count("XMAS")
    total_words += l.count("SAMX")


# diagonal
# we need 10
def check_adjacent_tiles(i, j, a, b, c):
    new_i = i + a
    new_j = j + b
    if new_i < 0 or new_i >= len(ls):
        return
    if new_j < 0 or new_j >= len(l):
        return
    if ls[new_i][new_j] == c:
        # Annoying hack
        if a > 0:
            a = 1
        else:
            a = -1
        if b > 0:
            b = 1
        else:
            b = -1
        return (a, b)


for i in range(len(ls)):
    for j in range(len(l)):
        if ls[i][j] == "X":
            vs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            m_s = []
            for x, y in vs:
                m = check_adjacent_tiles(i, j, x, y, "M")
                if m is not None:
                    m_s.append(m)
            a_s = []
            for x, y in m_s:
                a = check_adjacent_tiles(i, j, x * 2, y * 2, "A")
                if a is not None:
                    a_s.append(a)
            s_s = []
            for x, y in a_s:
                s = check_adjacent_tiles(i, j, x * 3, y * 3, "S")
                if s is not None:
                    s_s.append(s)
            print(s_s)
            total_words += len(s_s)

print(total_words)
