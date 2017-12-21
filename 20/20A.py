import sys

mina = -1
mini = -1
i = 0
for line in sys.stdin:
    pva = line.strip().split(', ')
    a = (pva[2].split('a=<')[1][:-1]).split(',')
    accel = int(a[0])**2 + int(a[1])**2 + int(a[2])**2
    if accel < mina or mina == -1:
        mina = accel
        mini = i
    i += 1

print(mini)
