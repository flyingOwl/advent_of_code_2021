import sys

lines = open(sys.argv[1]).readlines()

n = [ int(x) for x in lines[0].split(',') ]
b = {}
for i in range(len(lines) // 6):
	b[i] = [[int(x) for x in lines[2+i*6+j].split()] for j in range(5)]
	b[i] += [list(z) for z in zip(*b[i])]

def s(n,f):
	return n[-1] * sum(set(i for l in f[:5] for i in l) - set(n))

def x(n,b,m,i=5):
	r = [ max([len([ e for e in r if e in n[:i]]) for r in b[f]]) for f in b ]
	return 0 if min(r) == 5 and ~m else s(n[:i], b[r.index(5)]) if 5 in r and m else x(n,b,m,i+1) or s(n[:i+1], b[r.index(4)])

print("Part 1: {:d}".format(x(n,b,1)))
print("Part 2: {:d}".format(x(n,b,0)))
