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

idx = 1
total = 0
while True:
    left = eval(next(data))
    right = eval(next(data))
    left, right = coerced(left, right)
    if left < right:
        total += idx
    try:
        next(data)
    except StopIteration:
        break
    idx +=1
print(total)