def empty(position):
    if position.real in range(0, 7, 1):
        if position.imag > 0:
            if position not in tower:
                return True


def check(position, direction, rocks):
    tempEmpty = []

    for rock in rocks:
        tempEmpty.append(empty(position + direction + rock))

    return all(tempEmpty)

infile = open('input.txt').read()

rocks = (
    (0, 1, 2, 3),
    (1, 0+1j, 2+1j, 1+2j),
    (0, 1, 2, 2+1j, 2+2j),
    (0, 0+1j, 0+2j, 0+3j),
    (0, 1, 0+1j, 1+1j)
    )

x, y, top = 0, 0, 0
jets = []
tower = set()
visited = dict()

for line in infile:
    jets.append(ord(line)-61)

for step in range(0, 1000000000000, 1):
    position = complex(2, top + 4)

    if step == 2022: 
        print("Part A: " + str(int(top)))

    key = x,y

    if key in visited:
        S, T = visited[key]

        d, m = divmod(1000000000000 - step, step - S)

        if m == 0:
            print("Part B: " + str(int(top + (top - T) * d)))
            break
    else: 
        visited[key] = step, top

    rock = rocks[x]
    x = (x + 1) % len(rocks)

    while True:
        currentJet = jets[y]
        y = (y + 1) % len(jets)

        if check(position, currentJet, rock): 
            position += currentJet
        if check(position, -1j, rock): 
            position += -1j
        else: 
            break

    for i in rock:
        tower |= {position + i}
    
    top = max(top, position.imag + [1, 0, 2, 2, 3][x])