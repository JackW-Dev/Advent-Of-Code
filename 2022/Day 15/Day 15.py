import re
import portion as P

infile = open("input.txt").read()
lines = infile.strip().splitlines()
lowerLimit = 2000000
upperLimit = 4000000
multiplier = 4000000
partA = set()
partB = 0
beacons = set()

for line in lines:
    intValues = re.findall('-?\d+', line)
    sensorX = int(intValues[0])
    sensorY = int(intValues[1])
    beaconX = int(intValues[2])
    beaconY = int(intValues[3])

    if beaconY == lowerLimit:
        beacons.add(beaconX)
    if sensorY == lowerLimit:
        beacons.add(sensorX)

    distance = abs(sensorX-beaconX) + abs(sensorY-beaconY)

    rangeFlag = lowerLimit in range(sensorY, sensorY + distance + 1)
    rangeFlag2 = lowerLimit in range(sensorY - distance, sensorY)
        
    if rangeFlag or rangeFlag2:
        partA |= set(range(sensorX - distance + abs(lowerLimit-sensorY), sensorX + distance - abs(lowerLimit - sensorY) + 1))
    
partA -= beacons

reversedRange = reversed(range(upperLimit+1))

for i in reversedRange:
    notPossible = P.empty()
    
    for line in lines:
        intValues = re.findall('-?\d+', line)
        sensorX = int(intValues[0])
        sensorY = int(intValues[1])
        beaconX = int(intValues[2])
        beaconY = int(intValues[3])

        distance = abs(sensorX-beaconX) + abs(sensorY-beaconY)
        
        rangeFlag = lowerLimit in range(sensorY, sensorY+distance+1)
        rangeFlag2 = lowerLimit in range(sensorY-distance, sensorY)
        
        if rangeFlag or rangeFlag2:
            notPossible |= P.closed(max(0, sensorX - distance + abs(i - sensorY)), min(upperLimit + 1, sensorX + distance - abs(i - sensorY) + 1))
    
    if notPossible != P.closed(0, upperLimit + 1):
        partB = P.to_data(notPossible)[0][2] * multiplier + i
        break

print("Part A: " + str(len(partA)))
print("part B: " + str(partB))
