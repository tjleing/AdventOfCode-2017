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

processed = []
components = 0

def find_first_unprocessed():
    for i in range(len(adjlist)):
        if i not in processed:
            return i
    return -1

while True:
    start = find_first_unprocessed()
    if start == -1:
        break

    unprocessed = adjlist[start]

    while len(unprocessed) != 0:
        curr_node = unprocessed[0]
        unprocessed = unprocessed[1:]
        for neighbor in adjlist[curr_node]:
            if neighbor not in processed and neighbor not in unprocessed and neighbor != curr_node:
                unprocessed.append(neighbor)
        processed.append(curr_node)
    components += 1

print(components)
