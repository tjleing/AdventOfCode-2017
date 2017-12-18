import sys

instructions = []
registers = {}
for line in sys.stdin:
    instructions.append(line.split())

for reg in 'abcdefghijklmnopqrstuvwxyz':
    registers[reg] = 0

lastsnd = 0
index = 0
while True:
    print(index)
    #print(registers['a'])
    if instructions[index][0] == 'snd':
        try:
            lastsnd = int(instructions[index][1])
        except:
            lastsnd = registers[instructions[index][1]]
        index += 1

    elif instructions[index][0] == 'set':
        try:
            registers[instructions[index][1]] = int(instructions[index][2])
        except:
            registers[instructions[index][1]] = registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'add':
        try:
            registers[instructions[index][1]] += int(instructions[index][2])
        except:
            registers[instructions[index][1]] += registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'mul':
        try:
            registers[instructions[index][1]] *= int(instructions[index][2])
        except:
            registers[instructions[index][1]] *= registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'mod':
        try:
            registers[instructions[index][1]] %= int(instructions[index][2])
        except:
            registers[instructions[index][1]] %= registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'rcv':
        if instructions[index][1] != '0':
            print(lastsnd)
            break
        index += 1

    elif instructions[index][0] == 'jgz':
        try:
            if int(instructions[index][1]) > 0:
                try:
                    index += int(instructions[index][2])
                except:
                    index += registers[instructions[index][2]]
            else:
                index += 1
        except:
            if registers[instructions[index][1]] > 0:
                try:
                    index += int(instructions[index][2])
                except:
                    index += registers[instructions[index][2]]
            else:
                index += 1

