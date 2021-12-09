import sys

L = [ map(int,m.strip()) for m in open(sys.argv[1]).readlines() ]

A = {(x,y):v+1 for x,l in enumerate(L) for y,v in enumerate(l) if v < 9 }
q = lambda x,y: filter(A.get,[(x,y-1),(x,y+1),(x-1,y),(x+1,y),(x,y)])
d = {}

def n(c,l=[]):
	p = min(q(*c), key=A.get)
	if p == c:
		d[p] = d.get(p,set())|set(l)
	else:
		n(p,l+[c])

list(map(n,A))
a = sum(map(A.get,d))
b = sorted(len(d[x])+1 for x in d)[-3:]

print("Part 1: {:d}".format(a))
print("Part 2: {:d}".format(b[0]*b[1]*b[2]))
