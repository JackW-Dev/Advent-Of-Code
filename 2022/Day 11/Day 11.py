filein = open("input.txt", "r").read()
lines = filein.splitlines()

operation, testParam, conditions = [], [], []

for i in range(2, len(lines), 7):
    operation.append(lines[i][23:]) ## Stript out 'opeeration' starting at line 2, repeating every 7 lines - all conditions begin 'new = old ' so we can skip that part of the string

for i in range(3, len(lines), 7):
    testParam.append(int(lines[i][21:])) ## Stript out 'test paramaters' starting at line 3, repeating every 7 lines

for i in range(4, len(lines), 7):
    tempArr = []
    tempArr.append(int(lines[i][29:])) ## Append 'if true'
    tempArr.append(int(lines[i+1][30:])) ## Append 'if false'
    conditions.append(tempArr) ## Append conditions

modulo = 1
for i in testParam:
    modulo *= i

def calculate(part):
    inspections = [0 for _ in range(len(testParam))]
    items = [[[int(x) for x in (lines[y][18:]).split(", ")] for y in range(1, len(lines), 7)]][0]

    for _ in range(0, (20 if part == 1 else 10000 if part == 2 else 0)):
        for i in range(0, len(inspections)):
            for j in range(0, len(items[i])):
                current = items[i][j]
                if operation[i] == "* old":
                    current *= current
                elif operation[i][:2] == "* ":
                    current *= int(operation[i][2:])
                elif operation[i][:2] == "+ ":
                    current += int(operation[i][2:])
                current = current // 3 if part == 1 else current % modulo
                if current % testParam[i] == 0:
                    items[conditions[i][0]].append(current)
                else:
                    items[conditions[i][1]].append(current)
                inspections[i] += 1
            items[i] = []
    return sorted(inspections)[-1]*sorted(inspections)[-2]

print("Part A: " + str(calculate(1)))
print("Part B: " + str(calculate(2)))
