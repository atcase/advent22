data = open("input")

def coerced(l, r):
    if isinstance(l, list) and not isinstance(r, list):
        return coerced(l, [r])
    if not isinstance(l, list) and isinstance(r, list):
        return coerced([l], r)
    if isinstance(l, int) and isinstance(r, int):
        return l, r
    for idx in range(min(len(l), len(r))):
        l = l[:]
        r = r[:]
        l[idx], r[idx] = coerced(l[idx], r[idx])
    return l, r

class Packet(list):
    def __lt__(self, other):
        l, r = coerced(self, other)
        return list.__lt__(l, r)

packets = [[[2]], [[6]]]
for line in data:
    line = line.strip()
    if not line:
        continue
    packets.append(Packet(eval(line)))
packets.sort()

print((1 + packets.index([[2]])) * (1 + packets.index([[6]])))