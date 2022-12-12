from collections import Counter, defaultdict
from dataclasses import dataclass


@dataclass
class Monkey:
    items: list[int]
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
        return worry * arg // 3
    return (worry + arg) // 3

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

monkey_stats = Counter()
for round in range(20):
    for monkey_idx, monkey in monkeys.items():
        while monkey.items:
            worry = monkey.items.pop(0)
            worry = calc_next_worry(monkey.op, worry)
            if determine_test(monkey.test, worry):
                monkeys[monkey.next_monkey_if_true].items.append(worry)
            else:
                monkeys[monkey.next_monkey_if_false].items.append(worry)
            monkey_stats[monkey_idx] += 1
    for monkey_idx, monkey in monkeys.items():
        print(f"Monkey {monkey_idx}: {monkey.items}")

for monkey_idx, stat in monkey_stats.items():
    print(f"Monkey {monkey_idx} inspected items {stat} times.")

all_stats = list(sorted(monkey_stats.values()))
mb = all_stats[-1] * all_stats[-2]
print(f"Level of monkey business: {mb}")
