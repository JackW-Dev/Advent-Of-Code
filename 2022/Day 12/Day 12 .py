def charVal(char):
    if char not in "SE":
        return ord(char)
    elif char == 'S':
        return ord('a')
    else:
        return ord('z')

def breadthFirstSearch(arrToSearch):
    queue = [[arrToSearch]]
    seen = {arrToSearch}

    while queue:
        current = queue.pop(0)

        i, j = current[-1]

        if lineArr[i][j] == "E":
            return current

        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= x < len(lineArr):
                if 0 <= y < len(lineArr[0]):
                    if charVal(lineArr[x][y]) - charVal(lineArr[i][j]) < 2:
                        if (x, y) not in seen:
                            queue.append(current + [(x, y)])
                            seen.add((x, y))


infile = open("input.txt")
lines = infile.readlines()
lineArr = []

for line in lines:
    lineArr.append(list(line))


for vals in ['S', "aS"]:
    starts = [(i, j) for j in range(len(lineArr[0])) for i in range(len(lineArr)) if lineArr[i][j] in vals]
    print(min(len(path) - 1 for s in starts if (path := breadthFirstSearch(s)) is not None))

