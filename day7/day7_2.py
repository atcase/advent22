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

def dir_sizes(d, dir):
    sz = 0
    for k, v in dir.items():
        if k == "..":
            continue
        if isinstance(v, int):
            sz += v
        else:
            ksz, _ = yield from dir_sizes(k, v)
            sz += ksz
    yield sz, d
    return sz, d

all_dir_sizes = list(dir_sizes("/", root))
all_dir_sizes.sort()
total = 70000000
needed = 30000000
available = total - all_dir_sizes[-1][0]
shortfall = needed - available
print(f"total = {total}")
print(f"needed = {needed}")
print(f"available = {available}")
print(f"shortfall = {shortfall}")
for sz, candidate in all_dir_sizes:
    if sz >= shortfall:
        break
print(sz, candidate)

