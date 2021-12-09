import sys

L = [[int(i) for i in m.strip() ] for m in open(sys.argv[1]).readlines() ]

A = {(x,y):L[y][x]+1 for x in range(len(L[0])) for y in range(len(L)) if L[y][x]<9 }

q = lambda x,y: filter(A.get,[(x,y-1),(x,y+1),(x-1,y),(x+1,y),(x,y)])

d = {}
def n(l,c):
	p = min(q(*c), key=A.get)
	if p == c:
		d[p] = d[p]|set(l) if p in d else set(l)
	else:
		n(l+[c],p)

[n([],p) for p in A]
a = sum(A[p] for p in d.keys())
b = sorted(len(d[x])+1 for x in d)[-3:]

print("Part 1: {:d}".format(a))
print("Part 2: {:d}".format(b[0]*b[1]*b[2]))
