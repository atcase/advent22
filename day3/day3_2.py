data = open("input.txt")
total = 0
rucksacks = list(map(str.strip,data))
num_rucksacks = len(rucksacks)
for group in range(num_rucksacks//3):
    rucksack1 = rucksacks[group*3]
    rucksack2 = rucksacks[group*3 + 1]
    rucksack3 = rucksacks[group*3 + 2]
    badge = set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3)).pop()
    if badge == badge.lower():
        priority = 1 + ord(badge) - ord('a')
    else:
        priority = 27 + ord(badge) - ord('A')
    total += priority
print(total)
