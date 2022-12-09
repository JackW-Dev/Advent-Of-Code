with open("input.txt", "r") as infile:
    input_data = infile.readline().strip()

for i in range(len(input_data) - 4):
    if len(set(input_data[i:i+4])) == 4:
        print("Part A: " + str(i+4))
        break

for i in range(len(input_data) - 14):
    if len(set(input_data[i:i+14])) == 14:
        print("Part B: " + str(i+14))
        break