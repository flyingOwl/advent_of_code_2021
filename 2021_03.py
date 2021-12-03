import sys

lines = open(sys.argv[1]).readlines()

b = len(lines[0]) - 1
def m(i,l):
	return sum(int(l[i]) for l in l) >= len(l)/2.
g = sum(2**i * m(-2-i,lines) for i in range(b))
e = 2**b - 1 - g

def n(l,i,o):
	return l[0] if len(l) == 1 else n([ e for e in l if int(e[i]) ^ m(i,l) ^ o ], i+1, o)
x = int(n(lines,0,1),2)
c = int(n(lines,0,0),2)

print("Part 1: {:d}".format(e*g))
print("Part 2: {:d}".format(x*c))
