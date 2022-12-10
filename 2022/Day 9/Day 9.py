rope = [0] * 10
visited = [set([i]) for i in rope]
dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}

def value(distance):
    x = ((distance.real > 0) - (distance.real < 0))
    y = ((distance.imag > 0) - (distance.imag < 0))
    # print(x, y)
    return complex(x, y)

infile = open('input.txt')

for line in infile:
    for _ in range(0, int(line[2:]), 1):
        rope[0] += dirs[line[0]]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += value(dist)
                visited[i].add(rope[i])

print("Part A: " + str(len(visited[1])))
print("Part B: " + str(len(visited[9])))
