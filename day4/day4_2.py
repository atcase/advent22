data = open("input")
total = 0
for pair in data:
    regions = pair.split(",")
    ranges = [list(map(int, r.split("-"))) for r in regions]
    lsec, rsec = [set(range(r[0], r[1] + 1)) for r in ranges]
    if lsec.issubset(rsec) or lsec.issuperset(rsec):
        total += 1
print(total)
