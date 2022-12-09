def rotateMatrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

infile = open('input.txt')
treeArr = []

for line in infile:
    lineArr = list(line.strip())
    treeArr += [lineArr]

length = len(treeArr[0])
depth = len(treeArr)

partA = [[0 for i in range(0, length, 1)] for j in range(0, depth, 1)]
partB = [[1 for i in range(0, length, 1)] for j in range(0, depth, 1)]

for _ in range(0, 4, 1):
    for i, j in [(i, j) for i in range(0, length, 1) for j in range(0, depth, 1)]: 

        lower = []
        currArr = treeArr[i][j+1:]

        for val in currArr:
            lower.append(val < treeArr[i][j])

        partA[i][j] |= all(lower)

        if all(lower):
            partB[i][j] *= len(lower)
        else:
            partB[i][j] *= lower.index(0)+1

    treeArr = rotateMatrix(treeArr)
    partA = rotateMatrix(partA)
    partB = rotateMatrix(partB)

print("Part A:", sum(map(sum, partA)))
print("part B:", max(map(max, partB)))
