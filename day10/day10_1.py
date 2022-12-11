def addx(v):
    global x_reg
    yield
    x_reg += v
    yield

def noop():
    yield

def get_op_function(op):
    if op == "addx":
        return addx
    return noop

data = open("input")
x_reg = 1
signal_strength = [x_reg]
for instr in data:
    op, *args = instr.split()
    args = [int(a) for a in args]
    op_fn = get_op_function(op)
    for cycle in op_fn(*args):
        cycle_count = len(signal_strength) + 1
        signal_strength.append(cycle_count * x_reg)

total = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    ss = signal_strength[cycle - 1]
    total += ss
    print(cycle, ss, total)