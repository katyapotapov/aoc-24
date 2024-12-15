from time import sleep


with open("input_full.txt") as f:
# with open("input_2.txt") as f:
# with open("input.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

smol_warehouse = []
moves = ""
robot_pos = ""
boxes = []

for i in ls:
    if "#" in i:
        smol_warehouse.append(list(i))
    elif "<" in i:
        moves += i

print(robot_pos)
print(moves)

warehouse = []
for i in range(len(smol_warehouse)):
    s = ""
    for j in range(len(smol_warehouse[0])):
        if smol_warehouse[i][j] == "O":
            s += "[]"
        elif smol_warehouse[i][j] == "#":
            s += "##"
        elif smol_warehouse[i][j] == ".":
            s += ".."
        elif smol_warehouse[i][j] == "@":
            s += "@."
        else:
            raise Exception("you donked up")
    warehouse.append(s)

for i in range(len(warehouse)):
    s = ""
    for j in range(len(warehouse[0])):
        if warehouse[i][j] == "[":
            boxes.append((i, j))
        elif warehouse[i][j] == "]":
            continue
        elif warehouse[i][j] == "@":
            robot_pos = ((i, j))

def cur_viz():
    for i in range(len(warehouse)):
        viz_str = ""
        for j in range(len(warehouse[0])):
            if (i, j) == robot_pos:
                viz_str += ("@")
            elif (i, j) in boxes:
                viz_str += ("[")
            elif (i, j) in [(b[0], b[1]+1) for b in boxes]:
                viz_str += ("]")
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

def try_to_move_to(pos, move, is_robot = False, is_r_box = False):
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
        return [False]
    elif new_pos in boxes or (new_pos[0],new_pos[1]-1) in boxes:
        box_pos_to_remove = new_pos
        if (new_pos[0],new_pos[1]-1) in boxes:
            box_pos_to_remove = (new_pos[0], new_pos[1]-1)
        # Try to move this guy
        maybe_move_boxes = []
        if vec[0] != 0:
            l_maybe_boxes = try_to_move_to(box_pos_to_remove, move)
            r_maybe_boxes = try_to_move_to((box_pos_to_remove[0], box_pos_to_remove[1]+1), move, is_r_box = True)
            maybe_move_boxes += l_maybe_boxes
            maybe_move_boxes += r_maybe_boxes
        elif vec == (0, 1):
            r_maybe_boxes = try_to_move_to((box_pos_to_remove[0], box_pos_to_remove[1]+1), move, is_r_box = True)
            if r_maybe_boxes:
                maybe_move_boxes += r_maybe_boxes
        elif vec == (0, -1):
            maybe_move_boxes += try_to_move_to(box_pos_to_remove, move)

        if all(maybe_move_boxes) and len(maybe_move_boxes) > 0:
            maybe_move_boxes.append(box_pos_to_remove)
            maybe_move_boxes = list(set(maybe_move_boxes))
            if is_robot:
                return (pos, maybe_move_boxes)
            else:
                return maybe_move_boxes
        else:
            return [False]
    else:
        if is_robot:
            return (pos, [])
        elif is_r_box:
            return [True]
        else:
            return [pos]

def move_to(posses, move):
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

    new_posses = []
    for pos in posses:
        new_posses.append((pos[0] + vec[0], pos[1] + vec[1]))
    return new_posses

print(cur_viz())

for move in moves:
    maybe_poses = try_to_move_to(robot_pos, move, True)
    if maybe_poses != [False]:
        maybe_robot_new_pos, maybe_boxes_new_pos = maybe_poses
        robot_pos = move_to([maybe_robot_new_pos], move)[0]
        real_boxes = []
        for box in maybe_boxes_new_pos:
            if box is True:
                continue
            boxes.remove(box)
            real_boxes.append(box)
        # real_boxes = []
        # for box in maybe_boxes_new_pos:
        #     try:
        #         boxes.remove(box)
        #         real_boxes.append(box)
        #     except:
        #         pass
        boxes += move_to(real_boxes, move)

    # print(f"Move {move}")
    # cur_viz()
    # print()
    # print()

sum = 0
for box in boxes:
    sum += box[0] * 100 + box[1]

print(cur_viz())
print(sum)

