import sys

L = open(sys.argv[1]).read().splitlines()
P = {tuple(map(int,p.split(','))) for p in L if ',' in p}
C = [*map(max,zip(*P))]
F = []
for p in L[len(P)+1:]:
	C['y' in p] = int(p[13:])
	F += [[*C]]

b = lambda n,f: abs((n//f)%2*(f-2)-n%f)
f = lambda P,X,Y: {(b(x,X+1),b(y,Y+1)) for x,y in P}

X,Y=F[-1]
N=f(P,X,Y)

print("Part 1: {:d}".format(len(f(P,*F[0]))))
print("Part 2: \n{:s}".format('\n'.join(''.join(" #"[(x,y) in N] for x in range(X)) for y in range(Y))))
