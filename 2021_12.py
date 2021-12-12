import sys

L = open(sys.argv[1]).read().splitlines()
C = {}
S = "start"
def a(s,d):
	if d != S:
		C[s] = C.get(s,[])+[d]

for l in L:
	s,d = l.split('-')
	a(s,d)
	a(d,s)

def u(v,b):
	if 'end' in v:
		return [v]
	c = [(n in v and n.islower(),n) for n in C[v[-1]]]
	return [l for x,n in c if not(x&b) for l in u(v+[n],x|b)]

W = u([S],1)
U = u([S],0)
print("Part 1: {:d}".format(len(W)))
print("Part 2: {:d}".format(len(U)))
