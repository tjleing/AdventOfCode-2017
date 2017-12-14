import sys

parents = {}
randomname = ""

for line in sys.stdin:
    line = line.strip()
    line = line.split(" (")
    currentname = line[0]
    randomname = currentname
    remainder = line[1]
    remainder = remainder.split(") -> ")
    if len(remainder) == 2:
        # discard the weight (remainder[0])
        names = remainder[1]
        names = names.split(", ")
        for name in names:
            parents[name] = currentname

# we can find the root by continuously taking the parent of randomname
while randomname in parents:
    randomname = parents[randomname]

print(randomname)
