import sys

L = [ m.split('|') for m in open(sys.argv[1]).readlines() ]

m = [0,0,8,1,7,4]
M = lambda l,x: m[l] or 15-x[0]*9-x[1]*6 if l else 5-x[0]-x[1]*2

a = sum(sum(bool(m[len(x)-5]) for x in l[1].split()) for l in L)
b=0
for n,o in L:
	S = [set(c for c in n if n.count(c)==i) for i in m]
	e,c = *S[5], *S[2].intersection(min(n.split(),key=len))
	l = [str(M(len(O)-5,[e in O,c in O])) for O in o.split()]
	b+=int(''.join(l))

print("Part 1: {:d}".format(a))
print("Part 2: {:d}".format(b))
