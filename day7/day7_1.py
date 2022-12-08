data = open("input")
root = {}
cwd = root
line = next(data)
while True:
    prompt, cmd, *args = line.split()
    if cmd == "cd":
        if args[0] == "/":
            cwd = root
        else:
            cwd = cwd[args[0]]
    elif cmd == "ls":
        for line in data:
            if line.startswith("$"):
                break
            l, r = line.split()
            if l == "dir" and r not in cwd:
                cwd[r] = {"..": cwd}
            else:
                cwd[r] = int(l)
        else:
            break
        continue
    line = next(data)

def dir_sizes(dir: dict) -> int:
    sz = 0
    for k, v in dir.items():
        if k == "..":
            continue
        if isinstance(v, int):
            sz += v
        else:
            sz += yield from dir_sizes(v)
    yield sz
    return sz

total = 0
for sz in dir_sizes(root):
    if sz <= 100000:
        total += sz

print(total)
