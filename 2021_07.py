import sys

s = list(map(int,open(sys.argv[1]).read().split(",")))
r = range(max(s)+1)
i = 0
o = [(j,i:=i+j) for j in r ]
a = lambda f: min(sum(o[abs(n-x)][f] for n in s) for x in r)

print("Part 1: {:d}".format(a(0)))
print("Part 2: {:d}".format(a(1)))
