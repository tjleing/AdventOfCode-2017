import sys

scanner_ranges = []
for i in range(100):
    scanner_ranges.append(0)

for line in sys.stdin:
    line = line.split(": ")
    scanner_ranges[int(line[0])] = int(line[1])

severity = 0
for time in range(100):
    if scanner_ranges[time] != 0 and time % (2*scanner_ranges[time]-2) == 0:
        severity += time * scanner_ranges[time]
print(severity)
