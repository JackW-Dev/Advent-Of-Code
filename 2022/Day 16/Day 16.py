import re

def visit(valve, budget, state, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)
    for valveA in flowRates:
        newBudget = budget - valveMatches[valve][valveA] - 1
        if fromToValveCount[valveA] & state or newBudget <= 0: continue
        visit(valveA, newBudget, state | fromToValveCount[valveA], flow + newBudget * flowRates[valveA], answer)
    return answer  

infile = open("input.txt").read()
lines = infile.splitlines()

splitLines = []

for line in lines:
    splitLines.append(re.split('[\\s=;,]+', line))

valves = {}
flowRates = {}
fromToValveCount = {}
valveMatches = {}

for line in splitLines:
    valves.update({line[1]: set(line[10:])})

    if int(line[5]) != 0:
        flowRates.update({line[1]: int(line[5])})

for valve, flowRate in enumerate(flowRates):
    fromToValveCount.update({flowRate: 1<<valve})

for valve in valves:
    tempDict = {}

    for y in valves:
        if y in valves[valve]:
            tempDict.update({y: 1})
        else:
            tempDict.update({y: float('+inf')})

    valveMatches.update({valve: tempDict})

for i in valveMatches:
    for j in valveMatches:
        for k in valveMatches:
            valveMatches[j][k] = min(valveMatches[j][k], valveMatches[j][i]+valveMatches[i][k]) 

totalA = max(visit('AA', 30, 0, 0, {}).values())

visitedB = visit('AA', 26, 0, 0, {})

totalB = max(v1 + v2 for k1, v1 in visitedB.items() 
                   for k2, v2 in visitedB.items() if not k1 & k2)

print("Part A: " + str(totalA))
print("Part A: " + str(totalB))
