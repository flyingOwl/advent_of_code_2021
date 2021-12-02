import sys

d = [ int(l) for l in open(sys.argv[1]).readlines() ]
def answer(d, o):
    return sum([1 if v > d[i - o] else 0 for i,v in enumerate(d[o::], start=o)])

print("Part 1: {:d}".format(answer(d, 1)))
print("Part 2: {:d}".format(answer(d, 3)))
