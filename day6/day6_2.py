from collections import deque

data = open("input").read()
q = deque(maxlen=4)
for n, symbol in enumerate(data):
    q.append(symbol)
    if len(q) < 4:
        continue
    if len(set(q)) == 4:
        break
sop = n+1
# print(sop)
q = deque(maxlen=14)
for n, symbol in enumerate(data[sop:]):
    q.append(symbol)
    if len(q) < 14:
        continue
    if len(set(q)) == 14:
        break
som = sop + n + 1
print(som)
