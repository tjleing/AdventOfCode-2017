import sys

for line in sys.stdin:
    line = line.strip().split(",")
    position = list("abcdefghijklmnop")
    for token in line:
        if token[0] == 's':
            spinsize = int(token[1:])
            position = position[-spinsize:] + position[:-spinsize]
        elif token[0] == 'x':
            token = token[1:]
            token = token.split('/')
            firstpos = int(token[0])
            secondpos = int(token[1])
            temp = position[firstpos]
            position[firstpos] = position[secondpos]
            position[secondpos] = temp
        else:
            print(token)
            token = token[1:]
            token = token.split('/')
            for i in range(len(position)):
                if position[i] == token[0]:
                    firstpos = i
                if position[i] == token[1]:
                    secondpos = i
            temp = position[firstpos]
            position[firstpos] = position[secondpos]
            position[secondpos] = temp
print(position)
