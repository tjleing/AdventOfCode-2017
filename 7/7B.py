import sys

parents = {}
weights = {}
children = {}
randomname = ""

for line in sys.stdin:
    line = line.strip()
    line = line.split(" (")
    currentname = line[0]
    randomname = currentname
    remainder = line[1]
    remainder = remainder.split(") -> ")
    children[currentname] = []

    if len(remainder) == 1:
        weights[currentname] = int(remainder[0][:-1]) # strip off closing paren
    else:
        weights[currentname] = int(remainder[0])
        names = remainder[1]
        names = names.split(", ")
        for name in names:
            parents[name] = currentname
            children[currentname].append(name)

# we can find the root by continuously taking the parent of randomname
while randomname in parents:
    randomname = parents[randomname]
root = randomname

def sum_subtree(name):
    """ sums the weights of the subtree of root _name_ """
    total = weights[name]
    for child in children[name]:
        total += sum_subtree(child)
    return total


subtreetotals = []
for child in children[root]:
    subtreetotals.append(sum_subtree(child))
subtreetotals = sorted(subtreetotals)
differenttotal = -1
sametotal = subtreetotals[1]
if subtreetotals[0] != subtreetotals[1]:
    differenttotal = subtreetotals[0]
else:
    differenttotal = subtreetotals[-1]

different_root = ""
for i in range(len(children[root])):
    child = children[root][i]
    if sum_subtree(child) == differenttotal:
        different_root = child

def find_wrong_weight(wrong_root, supposed_to_be_total):
    if len(children[wrong_root]) == 0:
        return supposed_to_be_total

    subtreetotals = []
    for child in children[wrong_root]:
        subtreetotals.append(sum_subtree(child))

    all_same = True
    for i in range(len(subtreetotals)-1):
        if subtreetotals[i] != subtreetotals[i+1]:
            all_same = False
    if all_same:
        difference = sum_subtree(wrong_root) - supposed_to_be_total
        return weights[wrong_root] - difference

    supposed_to_be_total -= weights[wrong_root]
    supposed_to_be_total /= len(children[wrong_root])
    for i in range(len(subtreetotals)):
        if subtreetotals[i] != supposed_to_be_total:
            return find_wrong_weight(children[wrong_root][i], supposed_to_be_total)

print(find_wrong_weight(different_root, sametotal))
