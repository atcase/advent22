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
elf_calories.sort(reverse=True)
sum_top3 = sum(elf_calories[:3])
print(sum_top3)