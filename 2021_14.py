import sys

L = open(sys.argv[1]).read().splitlines()
T = [ L[0][i:i+2] for i in range(len(L[0])-1)]
P = { k:(k[0]+v,v+k[1]) for k,v in [ p.split(' -> ') for p in L[2:]]}
N = { k:T.count(k) for k in P}

def l(I,N,P):
	for i in range(I): N = {c:sum(N[j] for j in P if c in P[j]) for c in P}
	M = [(sum(v*k.count(c[0]) for k,v in N.items())+1)//2 for c in N]
	return max(M)-min(M)

print("Part 1: {:d}".format(l(10,N,P)))
print("Part 2: {:d}".format(l(40,N,P)))
