import sys

grid = []
linelength = 25
padding = 10000

for _ in range(padding):
    templine = []
    templine += (list('.'*(2*padding+linelength)))
    grid.append(templine)
for line in sys.stdin:
    templine = []
    templine += (list('.'*padding))
    templine += (list(line.strip()))
    templine += (list('.'*padding))
    grid.append(templine)
for _ in range(padding):
    templine = []
    templine += (list('.'*(2*padding+linelength)))
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
def reverse():
    direction[0] = -direction[0]
    direction[1] = -direction[1]

count = 0
for _ in range(10000000):
    if _ % 100000 == 0:
        print(_)
    if grid[position[0]][position[1]] == '.':
        # turn left and weaken
        grid[position[0]][position[1]] = 'W'
        left_turn()
        position[0] += direction[0]
        position[1] += direction[1]
    elif grid[position[0]][position[1]] == 'W':
        # don't turn and infect
        count += 1
        grid[position[0]][position[1]] = '#'
        position[0] += direction[0]
        position[1] += direction[1]
    elif grid[position[0]][position[1]] == '#':
        # turn right and flag
        grid[position[0]][position[1]] = 'F'
        right_turn()
        position[0] += direction[0]
        position[1] += direction[1]
    else:
        # reverse and clean
        grid[position[0]][position[1]] = '.'
        reverse()
        position[0] += direction[0]
        position[1] += direction[1]


print(count)
