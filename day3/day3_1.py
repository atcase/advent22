data = open("input.txt")
total = 0
for rucksack in data:
    rucksack = rucksack.strip()
    num_items = len(rucksack)
    first_compartment = rucksack[:num_items//2]
    second_compartment = rucksack[num_items//2:]
    extraneous_items = set(first_compartment).intersection(set(second_compartment))
    extraneous_item = extraneous_items.pop()
    if extraneous_item == extraneous_item.lower():
        priority = 1 + ord(extraneous_item) - ord('a')
    else:
        priority = 27 + ord(extraneous_item) - ord('A')
    total += priority
print(total)
