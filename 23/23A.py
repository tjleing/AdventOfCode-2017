import sys

instructions = []
registers = {}
for line in sys.stdin:
    instructions.append(line.split())

for reg in 'abcdefgh':
    registers[reg] = 0

muls = 0
index = 0
while True:
    if index >= len(instructions):
        break
    if instructions[index][0] == 'set':
        try:
            registers[instructions[index][1]] = int(instructions[index][2])
        except:
            registers[instructions[index][1]] = registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'sub':
        try:
            registers[instructions[index][1]] -= int(instructions[index][2])
        except:
            registers[instructions[index][1]] -= registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'mul':
        muls += 1
        try:
            registers[instructions[index][1]] *= int(instructions[index][2])
        except:
            registers[instructions[index][1]] *= registers[instructions[index][2]]
        index += 1

    elif instructions[index][0] == 'jnz':
        try:
            if int(instructions[index][1]) != 0:
                try:
                    index += int(instructions[index][2])
                except:
                    index += registers[instructions[index][2]]
            else:
                index += 1
        except:
            if registers[instructions[index][1]] != 0:
                try:
                    index += int(instructions[index][2])
                except:
                    index += registers[instructions[index][2]]
            else:
                index += 1

print(muls)
