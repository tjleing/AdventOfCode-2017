import sys

for line in sys.stdin:
    line = line.strip().split(",")
    position = list("abcdefghijklmnop")
    prevpositions = []
    for a in range(500):
        if a % 100 == 0:
            print a
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
        strpos = ''.join(position)
        if strpos in prevpositions:
            print strpos
            print a
        prevpositions.append(strpos)

# so the trick to this problem is that the programs' positions ends
# up forming a cycle of length 60.  I assumed that it had to be the
# case, but coded up the cycle-checker wrong.  Luckily, when I
# printed out the position at iteration 100 and 1000, they were the
# same, leading me to, on a whim, just submit it.  Magically, since
# 100 is congruent to 1000 which is congruent to 1000000000 (mod 60),
# it was right.  The cycle-checker works now though, so that's good.
