from time import sleep

# with open("input_full.txt") as f:
with open("input_full.txt") as f:

    ls = f.readlines()
ls = [l.strip() for l in ls]

not_visited = [(i, j) for i in range(len(ls)) for j in range(len(ls[0]))]


def get_all_adjacent_not_seen(i, j):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    adj = []
    for d in dirs:
        if (
            i + d[0] < len(ls)
            and i + d[0] >= 0
            and j + d[1] < len(ls[0])
            and j + d[1] >= 0
            and (i + d[0], j + d[1]) in not_visited
        ):
            adj.append((i + d[0], j + d[1]))
    return adj


def get_all_adjacent(i, j):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    adj = []
    for d in dirs:
        if (
            i + d[0] < len(ls)
            and i + d[0] >= 0
            and j + d[1] < len(ls[0])
            and j + d[1] >= 0
        ):
            adj.append((i + d[0], j + d[1]))
    return adj


def floodfill(i, j):
    frontier = get_all_adjacent_not_seen(i, j)
    plot = [(i, j)]
    while len(frontier) != 0:
        next_plot = frontier.pop()
        if ls[next_plot[0]][next_plot[1]] == ls[i][j]:
            try:
                not_visited.remove(next_plot)
            except ValueError:
                pass
            plot.append(next_plot)
            frontier += get_all_adjacent_not_seen(next_plot[0], next_plot[1])
    return plot


all_plots = []
while len(not_visited) > 0:
    next_plot = not_visited.pop()
    all_plots.append(floodfill(next_plot[0], next_plot[1]))

all_plots = [list(set(plots)) for plots in all_plots]

plots_to_perim = {}


def get_perim(plots):
    perim = 0
    for plot in plots:
        maybe_perim = get_all_adjacent(plot[0], plot[1])
        for i in maybe_perim:
            if ls[i[0]][i[1]] != ls[plot[0]][plot[1]]:
                perim += 1
        perim += 4 - len(maybe_perim)
    return perim



for p, plot in zip([get_perim(plots) for plots in all_plots], all_plots):
    print(f"{p=}, {len(plot)=}, {ls[plot[0][0]][plot[0][1]]=}")
    print(plot)

print(
    sum(
        [
            p * len(plot)
            for p, plot in zip([get_perim(plots) for plots in all_plots], all_plots)
        ]
    )
)
