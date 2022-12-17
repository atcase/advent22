
def print_cave():
    print("\33[H")
    for r in cave:
        print("".join(r))

def path_range(start, end):
    if start > end:
        start, end = end, start
    if start[0] == end[0]:
        return [(start[0], y) for y in range(start[1], end[1] + 1)]
    return [(x, start[1]) for x in range(start[0], end[0] + 1)]

data = open("input")
xs = [500]
ys = [0]
paths = []
for path_str in data:
    path_str = path_str.strip()
    path = []
    for point_str in path_str.split(" -> "):
        x, y = map(int, point_str.split(","))
        xs.append(x)
        ys.append(y)
        path.append((x, y))
    paths.append(path)
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)

# translate
for path in paths:
    for idx, (x, y) in enumerate(path):
        path[idx] = x-xmin, y-ymin
sand_x = 500 - xmin

cave_width = xmax - xmin + 1
cave_height = ymax + 1
cave = [["."] * cave_width for _ in range(cave_height)]

cave[0][sand_x] = "+"

# add the solid rock structure paths
for path in paths:
    for idx in range(len(path) - 1):
        start = path[idx]
        end = path[idx + 1]
        for pt in path_range(start, end):
            cave[pt[1]][pt[0]] = "#"


print_cave()

units_of_sand = 0
try:
    while True:
        sand_pos = sand_x, 0
        while True:
            x, y = sand_pos[0], sand_pos[1] + 1
            if cave[y][x] == ".":
                sand_pos = x, y
                continue
            x = x - 1
            if cave[y][x] == ".":
                sand_pos = x, y
                continue
            x = x + 2
            if cave[y][x] == ".":
                sand_pos = x, y
                continue
            break
        cave[sand_pos[1]][sand_pos[0]] = "o"
        units_of_sand += 1
        print_cave()
except IndexError:
    pass

print(units_of_sand)

