import sys

directions = []
for line in sys.stdin:
    line = line.strip()
    directions = line.split(",")

x=y=z=0
for direction in directions:
    # see http://keekerdc.com/wp-content/uploads/2011/03/HexGridLandscapeTriCoordinates.gif
    if direction == 'n':
        y += 1
        z -= 1
    if direction == 's':
        y -= 1
        z += 1
    if direction == 'ne':
        x += 1
        z -= 1
    if direction == 'sw':
        x -= 1
        z += 1
    if direction == 'nw':
        x -= 1
        y += 1
    if direction == 'se':
        x += 1
        y -= 1

print(max(x, max(y, z)))
