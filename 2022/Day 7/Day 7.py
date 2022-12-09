from collections import defaultdict

infile = open("input.txt").read().splitlines()
lines = map(str.split, infile)

path = []
dirs = defaultdict(int)

for value in lines:
    if value[0] == "$":
        if value[1] == "cd":
            if value[2] == "..":
                path.pop()
            else:
                path.append(value[2])
    elif value[0] != "dir":
        for i in range(len(path)):
            dirs[tuple(path[: i + 1])] += int(value[0])

partA = sum(size for size in dirs.values() if size <= 100000)

required = 30000000 - (70000000 - dirs[("/",)])

partB = min(size for size in dirs.values() if size >= required)

print("Part A: " + str(partA))
print("Part B: " + str(partB))