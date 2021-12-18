import sys
E=enumerate
N=[[[int(v),l[:i].count('[')-l[:i].count(']')] for i,v in E(l) if v.isdigit()] for l in open(sys.argv[1]).read().splitlines()]
V=lambda N:N.index(max(N,key=lambda v:v[1]))
def r(N):
	i=V(N);v,d=N[i]
	if d>4:
		if i>0:N[i-1][0]+=v
		if i+2<len(N):N[i+2][0]+=N[i+1][0]
		N[i:i+2]=[[0,d-1]];return(N,1)
	for i,(v,d) in E(N):
		if v>9:h=v//2;N[i:i+1]=[[h,d+1],[v-h,d+1]];return(N,1)
	return(N,0)

def a(A,B):
	R=[[v,d+1] for v,d in A+B];b=1
	while b:R,b=r(R)
	return R
def m(N):
	while len(N)>1:
		i=V(N);v,d=N[i]
		N[i:i+2]=[[3*v+2*N[i+1][0],d-1]]
	return N[0][0]
R=N[0]
for n in N[1:]:R=a(R,n);
I=range(len(N))
print("Part 1: {:d}".format(m(R)))
print("Part 2: {:d}".format(max(m(a(N[i],N[j])) for i in I for j in I if i!=j)))
