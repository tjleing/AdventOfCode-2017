import sys

grid = []
linelength = 25
padding = 1000

for _ in range(padding):
    templine = []
    templine += (list('.'*padding))
    templine += (list('.'*linelength))
    templine += (list('.'*padding))
    grid.append(templine)
for line in sys.stdin:
    templine = []
    templine += (list('.'*padding))
    templine += (list(line.strip()))
    templine += (list('.'*padding))
    grid.append(templine)
for _ in range(padding):
    templine = []
    templine += (list('.'*padding))
    templine += (list('.'*linelength))
    templine += (list('.'*padding))
    grid.append(templine)

position = [len(grid)/2, len(grid[0])/2]
direction = [-1, 0]

def right_turn():
    if direction[0] != 0:
        if direction[0] == 1:
            direction[1] = -1
        else:
            direction[1] = 1
        direction[0] = 0
    else:
        if direction[1] == 1:
            direction[0] = 1
        else:
            direction[0] = -1
        direction[1] = 0
def left_turn():
    if direction[0] != 0:
        if direction[0] == 1:
            direction[1] = 1
        else:
            direction[1] = -1
        direction[0] = 0
    else:
        if direction[1] == 1:
            direction[0] = -1
        else:
            direction[0] = 1
        direction[1] = 0

count = 0
for _ in range(10000):
    if grid[position[0]][position[1]] == '.':
        count += 1
        # turn left and infect
        grid[position[0]][position[1]] = '#'
        left_turn()
        position[0] += direction[0]
        position[1] += direction[1]
    else:
        # turn right and clean
        grid[position[0]][position[1]] = '.'
        right_turn()
        position[0] += direction[0]
        position[1] += direction[1]

print(count)
