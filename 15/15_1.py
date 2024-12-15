from time import sleep


with open("input_full.txt") as f:
# with open("input.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

warehouse = []
moves = ""
robot_pos = ""
boxes = []

for i in ls:
    if "#" in i:
        warehouse.append(list(i))
        if "@" in i:
            robot_pos = (ls.index(i), i.index("@"))
    elif "<" in i:
        moves += i

print(robot_pos)
print(moves)

for i in range(len(warehouse)):
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == "O":
            boxes.append((i, j))

def cur_viz():
    for i in range(len(warehouse)):
        viz_str = ""
        for j in range(len(warehouse[0])):
            if (i, j) == robot_pos:
                viz_str += ("@")
            elif (i, j) in boxes:
                viz_str += ("O")
            elif warehouse[i][j] == "#":
                viz_str += ("#")
            else:
                viz_str += (".")
        print(viz_str)

def is_in_grid(i, j):
    if (
        i< len(warehouse)
        and i>= 0
        and j< len(warehouse[0])
        and j>= 0
    ):
        return True
    return False

def try_to_move_to(pos, move):
    vec = None
    if move == "<":
        vec = (0, -1)
    elif move == ">":
        vec = (0, 1)
    elif move == "^":
        vec = (-1, 0)
    elif move == "v":
        vec = (1, 0)
    else:
        raise Exception("Wat is dis")

    new_pos = (pos[0] + vec[0], pos[1] + vec[1])
    if not is_in_grid(new_pos[0], new_pos[1]):
        raise Exception("Not in grid bro u messed up")
    if warehouse[new_pos[0]][new_pos[1]] == "#":
        # Nothing happens if we up against a wall, don't move
        return False
    elif new_pos in boxes:
        # Try to move this guy
        maybe_new_pos = try_to_move_to(new_pos, move)
        if maybe_new_pos:
            boxes.remove(new_pos)
            boxes.append(maybe_new_pos)
            return new_pos
        else:
            return False
    else:
        return new_pos


for move in moves:
    maybe_robot_new_pos = try_to_move_to(robot_pos, move)
    if maybe_robot_new_pos:
        robot_pos = maybe_robot_new_pos
    # print(f"Move {move}")
    # cur_viz()
    # print()
    # print()

sum = 0
for box in boxes:
    sum += box[0] * 100 + box[1]

print(cur_viz())
print(sum)

