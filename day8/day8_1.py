data = open("input")
trees = [tuple(map(int, line.strip())) for line in data]
trees_transpose = list(zip(*trees))
height = len(trees)
width = len(trees[0])

def adjacent_heights(x, y):
    row = trees[y]
    col = trees_transpose[x]
    yield row[:x]
    yield row[x+1:]
    yield col[:y]
    yield col[y+1:]

def is_visible(x, y) -> bool:
    h = trees[y][x]
    for direction in adjacent_heights(x, y):
        if all(h > ah for ah in direction):
            return True
    return False

num_visible = 0
for x in range(width):
    for y in range(height):
        if is_visible(x, y):
            num_visible += 1

print(num_visible)
