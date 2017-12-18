import sys

instructions = []
registers = [{}, {}]
for line in sys.stdin:
    instructions.append(line.split())

for reg in 'abcdefghijklmnopqrstuvwxyz':
    registers[0][reg] = 0
    registers[1][reg] = 0
registers[1]['p'] = 1

send = [[], []]
index = [0,0]
lastindex = [0,0]
sentby1 = 0
while True:
    lastindex[0] = index[0]
    lastindex[1] = index[1]
    for i in range(2):
        if instructions[index[i]][0] == 'snd':
            try:
                send[1-i].append(int(instructions[index[i]][1]))
            except:
                send[1-i].append(registers[i][instructions[index[i]][1]]
)
            if i == 1:
                sentby1 += 1
            index[i] += 1

        elif instructions[index[i]][0] == 'set':
            try:
                registers[i][instructions[index[i]][1]] = int(instructions[index[i]][2])
            except:
                registers[i][instructions[index[i]][1]] = registers[i][instructions[index[i]][2]]
            index[i] += 1

        elif instructions[index[i]][0] == 'add':
            try:
                registers[i][instructions[index[i]][1]] += int(instructions[index[i]][2])
            except:
                registers[i][instructions[index[i]][1]] += registers[i][instructions[index[i]][2]]
            index[i] += 1

        elif instructions[index[i]][0] == 'mul':
            try:
                registers[i][instructions[index[i]][1]] *= int(instructions[index[i]][2])
            except:
                registers[i][instructions[index[i]][1]] *= registers[i][instructions[index[i]][2]]
            index[i] += 1

        elif instructions[index[i]][0] == 'mod':
            try:
                registers[i][instructions[index[i]][1]] %= int(instructions[index[i]][2])
            except:
                registers[i][instructions[index[i]][1]] %= registers[i][instructions[index[i]][2]]
            index[i] += 1

        elif instructions[index[i]][0] == 'rcv':
            if len(send[i]) != 0:
                registers[i][instructions[index[i]][1]] = send[i][0]
                send[i] = send[i][1:]
                index[i] += 1

        elif instructions[index[i]][0] == 'jgz':
            try:
                if int(instructions[index[i]][1]) > 0:
                    try:
                        index[i] += int(instructions[index[i]][2])
                    except:
                        index[i] += registers[i][instructions[index[i]][2]]
                else:
                    index[i] += 1
            except:
                if registers[i][instructions[index[i]][1]] > 0:
                    try:
                        index[i] += int(instructions[index[i]][2])
                    except:
                        index[i] += registers[i][instructions[index[i]][2]]
                else:
                    index[i] += 1

    if index[0] == lastindex[0] and index[1] == lastindex[1]:
        # deadlock
        break

print(sentby1)
