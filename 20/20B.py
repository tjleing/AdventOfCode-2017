import sys
import copy

particles = []
for line in sys.stdin:
    pva = line.strip().split(', ')
    p = (pva[0].split('p=<')[1][:-1]).split(',')
    p = map(int, p)
    v = (pva[1].split('v=<')[1][:-1]).split(',')
    v = map(int, v)
    a = (pva[2].split('a=<')[1][:-1]).split(',')
    a = map(int, a)
    particles.append([p,v,a])

def magnitude(arr):
    return arr[0]**2+arr[1]**2+arr[2]**2

willsurvive = []
for i in particles:
    willsurvive.append(True)


for i in range(len(particles)):
    print(i)
    for j in range(len(particles)):
        if i == j:
            continue
        if magnitude(particles[i][2]) > magnitude(particles[j][2]) or (magnitude(particles[i][2]) == magnitude(particles[j][2]) and magnitude(particles[i][1]) > magnitude(particles[j][1])):
            continue
        # so j's acceleration (or velocity) is bigger, and if j ever gets further away than i does, then no collision
        pvai = copy.deepcopy(particles[i])
        pvaj = copy.deepcopy(particles[j])
        steps = 0
        while magnitude(pvai[0]) > magnitude(pvaj[0]):
            if steps > 1000:
                break
            for k in range(3):
                pvai[1][k] += pvai[2][k]
                pvai[0][k] += pvai[1][k]

                pvaj[1][k] += pvaj[2][k]
                pvaj[0][k] += pvaj[1][k]
            steps += 1
        if pvai[0] == pvaj[0]:
            willsurvive[i] = False
            willsurvive[j] = False

surviving = 0
for i in willsurvive:
    if i:
        surviving += 1

print(surviving)
