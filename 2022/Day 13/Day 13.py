from functools import cmp_to_key
from math import prod

def compare(leftHalf, rightHalf):
    match leftHalf, rightHalf:
        case int(), int():  return (leftHalf>rightHalf) - (leftHalf<rightHalf)
        case int(), list(): return compare([leftHalf], rightHalf)
        case list(), int(): return compare(leftHalf, [rightHalf])
        case list(), list():
            for i in map(compare, leftHalf, rightHalf):
                if i: return i
            return compare(len(leftHalf), len(rightHalf))

infile = open('input.txt').read()
lines = infile.split('\n\n')

split, splitB, toSum, toProd = [], [], [], []

for line in lines:
    values = [*map(eval, line.split())]
    split.append(values)
    splitB.append(values)

for i, j in enumerate(split, 1):
    if compare(*j) == -1:
        toSum.append(i)

splitBSum = sum(splitB, [[2], [6]])
splitB = sorted(splitBSum, key=cmp_to_key(compare))

for i, j in enumerate(splitB, 1):
    if j in [[2], [6]]:
        toProd.append(i)


print("Part A: " + str(sum(toSum)))
print("Part B: " + str(prod(toProd)))
