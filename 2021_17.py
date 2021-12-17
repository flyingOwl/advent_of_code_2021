import sys
A,B=[list(map(int,s.split(".."))) for s in open(sys.argv[1]).read()[15:-1].split(", y=")]

def h(a,y,m,u,v):
	n=set();s=b=0
	while [s<u and b<=m,s>u][y]:
		if [s>=v,s<=v][y]:n|={b}
		s+=a;b+=1;a-=bool(a or y)
	return n
H=lambda Q,P,y,m:{i:h(i,y,m,Q,P[y]) for i in range(Q*y,abs(Q))}
Y=H(B[0]-1,B,1,0)
X=H(A[1]+1,A,0,A[1])
z=B[0]+1
print("Part 1: {:d}".format(z*(z-1)//2))
print("Part 2: {:d}".format(sum(1 for x in X for y in Y if Y[y]&X[x])))
