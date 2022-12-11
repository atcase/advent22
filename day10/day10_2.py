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
x_values = [x_reg]
for instr in data:
    op, *args = instr.split()
    args = [int(a) for a in args]
    op_fn = get_op_function(op)
    for cycle in op_fn(*args):
        x_values.append(x_reg)

row = ""
for cycle, x_value in enumerate(x_values):
    scan_pos = cycle % 40
    if x_value - 1 <= scan_pos <= x_value + 1:
        row += "#"
    else:
        row += "."
    if scan_pos == 39:
        print(row)
        row = ""
