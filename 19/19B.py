import sys

grid = []
for line in sys.stdin:
    grid.append(line)

position = [0,99]
direction = [1,0]

steps = 0

while True:
    steps += 1
    position[0] += direction[0]
    position[1] += direction[1]

    if grid[position[0]][position[1]] == '|' or grid[position[0]][position[1]] == '-':
        # keep going
        pass
    elif grid[position[0]][position[1]] == '+':
        # change directions
        if direction[0] == 0:
            # traveling horizontally, turn vertical
            if grid[position[0]+1][position[1]] == ' ':
                direction = [-1,0]
            else:
                direction = [1,0]
        else:
            # traveling vertically, turn horizontal
            if grid[position[0]][position[1]+1] == ' ':
                direction = [0,-1]
            else:
                direction = [0,1]

    else:
        if grid[position[0]][position[1]] == ' ':
            break

print(steps)
