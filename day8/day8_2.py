data = open("input")
trees = [tuple(map(int, line.strip())) for line in data]
trees_transpose = list(zip(*trees))
height = len(trees)
width = len(trees[0])

def adjacent_heights(x, y):
    row = trees[y]
    col = trees_transpose[x]
    yield reversed(row[:x])
    yield row[x+1:]
    yield reversed(col[:y])
    yield col[y+1:]

def calc_scenic_score(x, y) -> int:
    h = trees[y][x]
    scenic_score = 1
    for direction in adjacent_heights(x, y):
        view_distance = 0
        for view_distance, ah in enumerate(direction, start=1):
            if ah >= h:
                break
        scenic_score *= view_distance
    return scenic_score

max_scenic_score = 0
for x in range(width):
    for y in range(height):
        scenic_score = calc_scenic_score(x, y)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
