data = open("input")
stacks = [[] for _ in range(9)]

for line in data:
    if "[" not in line:
        break
    crates = [line[n] for n in range(1, 2+8*4, 4)]
    for n, crate in enumerate(crates):
        if crate != " ":
            stacks[n].insert(0, crate)

next(data)
for line in data:
    _, num, _, src, _, dst = line.split()
    num=int(num)
    src=int(src)
    dst=int(dst)
    crates = stacks[src-1][-num:]
    del stacks[src-1][-num:]
    stacks[dst-1].extend(crates)

tops = [stack[-1] for stack in stacks]
print("".join(tops))
