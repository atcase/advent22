direction_delta = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}

def sign(n):
    if n == 0:
        return 0
    return 1 if n > 0 else -1

def tail_next(head, tail):
    delta = (head[0] - tail[0], head[1] - tail[1])
    if max(map(abs, delta)) < 2:
        return tail
    return tail[0] + sign(delta[0]), tail[1] + sign(delta[1])


data = open("input")
head = (0,0)
body = [(0,0)] * 9
tail_positions = set()
tail_positions.add((0,0))
for line in data:
    direction, num_steps = line.split()
    for _ in range(int(num_steps)):
        dd = direction_delta[direction]
        head = head[0] + dd[0], head[1] + dd[1]
        prev = head
        for n in range(len(body)):
            body[n] = tail_next(prev, body[n])
            prev = body[n]
        tail_positions.add(body[-1])

print(len(tail_positions))
