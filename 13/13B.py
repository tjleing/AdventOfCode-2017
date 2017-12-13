import sys

scanner_ranges = []
for i in range(100):
    scanner_ranges.append(0)

for line in sys.stdin:
    line = line.split(": ")
    scanner_ranges[int(line[0])] = int(line[1])

works = False
delay = 0
while not works:
    works = True
    for time in range(100):
        if scanner_ranges[time] != 0 and (time+delay) % (2*scanner_ranges[time]-2) == 0:
            works = False
        if not works:
            break

    print(delay)
    
    if not works:
        delay += 1

print(delay)
