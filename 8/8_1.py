from collections import defaultdict

with open("input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]


unique_freqs = set("".join(ls))
unique_freqs.remove(".")

freq_to_locs = defaultdict(list)
for i, l in enumerate(ls):
    for j, c in enumerate(l):
        freq_to_locs[c].append((i, j))

freq_to_locs.pop(".")


def eucl_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


def line(pt1, pt2):
    dist_x = pt1[0] - pt2[0]
    dist_y = pt1[1] - pt2[1]
    all_pts = []
    # for i in range(1, 100):
    return [
        (pt1[0] + dist_x, pt1[1] + dist_y),
        (pt2[0] - dist_x, pt2[1] - dist_y),
    ]
    # all_pts += [
    #     (pt1[0] + dist_x * i, pt1[0] + dist_y * i),
    #     (pt2[0] - dist_x * i, pt2[0] - dist_y * i),
    # ]

    # return all_pts


antinode_locs = set()
for freq, locs in freq_to_locs.items():
    for i_loc in range(len(locs)):
        for j_loc in range(i_loc + 1, len(locs)):
            # print(f"{(i, j)=}: {eucl_dist((i, j), locs[i_loc])}")
            line_pts = line(locs[i_loc], locs[j_loc])
            for pt in line_pts:
                if pt == locs[i_loc] or pt == locs[j_loc]:
                    continue
                # i_dist = eucl_dist(pt, locs[i_loc])
                # j_dist = eucl_dist(pt, locs[j_loc])
                # if i_dist / j_dist != 2 and j_dist / i_dist != 2:
                #     continue
                if pt[0] >= 0 and pt[0] < len(ls) and pt[1] >= 0 and pt[1] < len(ls[0]):
                    antinode_locs.add(pt)


print(sorted(list(antinode_locs)))
print(len(antinode_locs))

# antinode_locs = set()
# for i in range(len(ls)):
#     for j in range(len(ls[0])):
#         for freq, locs in freq_to_locs.items():
#             for i_loc in range(len(locs)):
#                 for j_loc in range(i_loc + 1, len(locs)):
#                     # print(f"{(i, j)=}: {eucl_dist((i, j), locs[i_loc])}")
#                     first_dist = eucl_dist((i, j), locs[i_loc])
#                     second_dist = eucl_dist((i, j), locs[j_loc])
#                     if (
#                         first_dist != 0
#                         and second_dist != 0
#                         and (
#                             first_dist / second_dist == 2
#                             or second_dist / first_dist == 2
#                         )
#                     ):
#                         antinode_locs.add((i, j))
#
#
# print(antinode_locs)
# print(len(antinode_locs))
