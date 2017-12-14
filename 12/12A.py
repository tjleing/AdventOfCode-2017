import sys

adjlist = []

for line in sys.stdin:
    line = line.strip()
    adjlist.append([])
    line = line.split(" <-> ")
    node = int(line[0])
    connected = line[1]
    connected = connected.split(", ")
    for neighbor in connected:
        adjlist[node].append(int(neighbor))

connected_component = [0]
unprocessed = adjlist[0]

while len(unprocessed) != 0:
    curr_node = unprocessed[0]
    unprocessed = unprocessed[1:]
    for neighbor in adjlist[curr_node]:
        if neighbor not in connected_component and neighbor not in unprocessed and neighbor != curr_node:
            unprocessed.append(neighbor)
    connected_component.append(curr_node)

print(len(connected_component))
