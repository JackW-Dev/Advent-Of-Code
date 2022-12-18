def rangeSorted(*value):
    return range(min(value), max(value) + 1)

def pathCheck(checkFlag):
    path = [500]
    rock = len(blocked)

    if checkFlag == 'A':
        check = lambda position: position.imag > floor
    elif checkFlag == 'B':
        check = lambda position: position == 500
        
    while True:
        position = path[-1]
        for dest in position + 1j, position - 1 + 1j, position + 1 + 1j:
            if dest not in blocked:
                if dest.imag < floor + 2:
                    path.append(dest)
                    break
        else:
            if check(position): 
                return len(blocked) - rock
            blocked.add(position)
            del path[-1]

blocked = set()

infile = open('input.txt')
lines = []

for line in infile:
    lines.append([*map(eval, line.split('->'))])

for line in lines:
    for (a, b), (c, d) in zip(line, line[1:]):
        blocked |= {complex(i, j) for i in rangeSorted(a, c)
                                  for j in rangeSorted(b, d)}

floor = []

for i in blocked:
    floor.append(i.imag)

floor = max(floor)

print("Part A: " + str(pathCheck('A')))
print("Part B: " + str(pathCheck('B') + 1))