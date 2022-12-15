data = open("input")
rows = []
for row_idx, line in enumerate(data):
    line = line.strip()
    if "S" in line:
        col_idx = line.index("S")
        start_pos = col_idx, row_idx
    if "E" in line:
        col_idx = line.index("E")
        end_pos = col_idx, row_idx
    line = line.translate(str.maketrans("SE", "az"))
    heights = [ord(x) - ord("a") for x in line]
    rows.append(heights)

map_height = len(rows)
map_width = len(rows[0])

distances = [[None] * map_width for _ in range(map_height)]

def print_it():
    print("\33[H")
    for row in distances:
        print(*[f"{d:3d}" if d is not None else "  ." for d in row])
    # input()

to_check = [(end_pos, 0)]
while to_check:
    (x, y), d = to_check.pop(0)
    height = rows[y][x]
    if height == 0:
        # Found it
        print(d)
        break
    if distances[y][x] is not None:
        # Already been here
        continue
    # print_it()
    distances[y][x] = d
    if x > 0 and height - rows[y][x - 1] <= 1:
        to_check.append(((x - 1, y), d + 1))
    if y > 0 and height - rows[y - 1][x] <= 1:
        to_check.append(((x, y - 1), d + 1))
    if x < map_width - 1 and height - rows[y][x + 1] <= 1:
        to_check.append(((x + 1, y), d + 1))
    if y < map_height - 1 and height - rows[y + 1][x] <= 1:
        to_check.append(((x, y + 1), d + 1))