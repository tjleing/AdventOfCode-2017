import sys

image = [[".","#","."], [".",".","#"], ["#","#","#"]]


def rotate(img):
    newimage = []
    for _ in range(len(img)):
        new = []
        for __ in range(len(img)):
            new.append('.')
        newimage.append(new)

    for i in range(len(img)):
        for j in range(len(img)):
            newimage[len(img)-1-j][i] = img[i][j]
    return newimage

def flip(img):
    newimage = []
    for _ in range(len(img)):
        new = []
        for __ in range(len(img)):
            new.append('.')
        newimage.append(new)

    for i in range(len(img)):
        for j in range(len(img)):
            newimage[len(img)-1-i][j] = img[i][j]
    return newimage

rules2 = []
rules3 = []
for line in sys.stdin:
    rule = line.strip().split(" => ")
    first = rule[0].split("/")
    first = map(list, first)
    second = rule[1].split("/")
    second = map(list, second)
    if len(first) == 2:
        for i in range(4):
            rules2.append([first, second])
            first = rotate(first)
        first = flip(first)
        for i in range(4):
            rules2.append([first, second])
            first = rotate(first)
    else:
        for i in range(4):
            rules3.append([first, second])
            first = rotate(first)
        first = flip(first)
        for i in range(4):
            rules3.append([first, second])
            first = rotate(first)

for step in range(18):
    print(step)
    if len(image) % 2 == 0:
        newimage = []
        for _ in range(len(image)*3/2):
            new = []
            for __ in range(len(image)*3/2):
                new.append('.')
            newimage.append(new)

        for i in range(len(image)/2):
            for j in range(len(image)/2):
                #segment = image[2*i:2*i+2][2*j:2*j+2]
                segment = [image[ii][2*j:2*j+2] for ii in range(2*i,2*i+2)]
                for rule in rules2:
                    if rule[0] == segment:
                        for ii in range(3*i,3*i+3):
                            for jj in range(3*j,3*j+3):
                                newimage[ii][jj] = rule[1][ii-3*i][jj-3*j]
                        #newimage[3*i:3*i+3][3*j:3*j+3] = rule[1]
                        break
        image = newimage
    else:
        newimage = []
        for _ in range(len(image)*4/3):
            new = []
            for __ in range(len(image)*4/3):
                new.append('.')
            newimage.append(new)

        for i in range(len(image)/3):
            for j in range(len(image)/3):
                #segment = image[3*i:3*i+3][3*j:3*j+3]
                segment = [image[ii][3*j:3*j+3] for ii in range(3*i,3*i+3)]
                for rule in rules3:
                    #print(rule[0])
                    if rule[0] == segment:
                        for ii in range(4*i,4*i+4):
                            for jj in range(4*j,4*j+4):
                                newimage[ii][jj] = rule[1][ii-4*i][jj-4*j]
                        #newimage[4*i:4*i+4][4*j:4*j+4] = rule[1]
                        break
        image = newimage

total = 0
for i in image:
    for j in i:
        if j == '#':
            total += 1
print(total)
