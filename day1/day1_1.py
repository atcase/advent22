data = open("input")
elf_calories = []
total = 0
for line in data:
    line = line.strip()
    if not line:
        elf_calories.append(total)
        total = 0
        continue
    total = total + int(line)
max_calories = max(elf_calories)
print(max_calories)
