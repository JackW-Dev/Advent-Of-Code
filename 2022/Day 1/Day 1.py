# Day 1 - Elf Snacks

infile = open("input.txt").read()
calories_totals = []

for line in infile.split("\n\n"):
    calories_totals.append(sum(eval(i) for i in line.splitlines()))

calories_totals = sorted(calories_totals)

print("Part A:", calories_totals[-1])
print("Part B:", sum(calories_totals[-3:]))