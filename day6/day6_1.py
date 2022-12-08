from collections import deque

data = open("input")
q = deque(maxlen=4)
for n, symbol in enumerate(data.read()):
    q.append(symbol)
    if len(q) < 4:
        continue
    if len(set(q)) == 4:
        break
print(n+1)
