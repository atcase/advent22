from collections import Counter, defaultdict
from dataclasses import dataclass


class Worry:
    def __init__(self, initial_worries):
        self._worries = initial_worries

    def __add__(self, rhs):
        result = {}
        for mod, val in self._worries.items():
            result[mod] = (val + rhs) % mod
        return Worry(result)

    def __mul__(self, rhs):
        result = {}
        for mod, val in self._worries.items():
            result[mod] = (val * rhs) % mod
        return Worry(result)
    
    def __rmul__(self, rhs):
        return self.__mul__(rhs)

    def __mod__(self, rhs):
        return self._worries[rhs] % rhs


@dataclass
class Monkey:
    items: list[int | Worry]
    op: str
    test: str
    next_monkey_if_true: str
    next_monkey_if_false: str

def calc_next_worry(operation: str, worry: int):
    _, op, arg = operation.rsplit(maxsplit=2)
    
    if arg == "old":
        arg = worry
    else:
        arg = int(arg)
    if op == "*":
        return worry * arg
    return (worry + arg)

def determine_test(test: str, worry: int):
    _, divisor = test.rsplit(maxsplit=1)
    return worry % int(divisor) == 0

monkeys : dict[str, Monkey] = {}

data = open("input")
lines = map(str.strip, iter(data))
while True:
    try:
        line = next(lines)
    except StopIteration:
        break
    if not line:
        continue
    assert line.startswith("Monkey"), f"{line!r}"
    monkey_idx = line.split(": ")[0][:-1].split()[1]
    items = [int(it) for it in next(lines).split(": ")[1].split(", ")]
    op = next(lines).split(": ")[1]
    test = next(lines).split(": ")[1]
    next_monkey_if_true = next(lines).split(": ")[1].split()[-1]
    next_monkey_if_false = next(lines).split(": ")[1].split()[-1]
    monkeys[monkey_idx] = Monkey(items, op, test, next_monkey_if_true, next_monkey_if_false)
print(f"Found {len(monkeys)} monkeys")

divisors = [m.test.rsplit(maxsplit=1)[1] for m in monkeys.values()]
for m in monkeys.values():
    m.items = [Worry({int(d): it for d in divisors}) for it in m.items]

monkey_stats = Counter()
for round in range(10000):
    for monkey_idx, monkey in monkeys.items():
        while monkey.items:
            worry = monkey.items.pop(0)
            worry = calc_next_worry(monkey.op, worry)
            if determine_test(monkey.test, worry):
                monkeys[monkey.next_monkey_if_true].items.append(worry)
            else:
                monkeys[monkey.next_monkey_if_false].items.append(worry)
            monkey_stats[monkey_idx] += 1

for monkey_idx, stat in monkey_stats.items():
    print(f"Monkey {monkey_idx} inspected items {stat} times.")

all_stats = list(sorted(monkey_stats.values()))
mb = all_stats[-1] * all_stats[-2]
print(f"Level of monkey business: {mb}")
