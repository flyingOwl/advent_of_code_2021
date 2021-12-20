import sys

L=[s.strip() for s in open(sys.argv[1]).read().split("---") if "," in s]
B,*N=[{tuple(map(int,l.split(','))) for l in s.split('\n')} for s in L]
I=set(range(len(N)))
T=lambda i,x,y,z:t(i//8,[x,-x][i&4>0],[y,-y][i&2>0],[z,-z][i&1])
t=lambda i,x,y,z:([x,y,z][i//2],[y,z,x,y][(i+1)//2],[z,y,x][i%3])
a=lambda A,B:tuple(map(sum,zip(A,B)))

S={-1:(0,0,0)}
while I:
	I-=S.keys()
	for i in I:
		for j in range(48):
			Z=[a(p,T(j,*q)) for p in B for q in N[i]];C={}
			for z in Z:C[z]=C.get(z,0)+1
			D=max(C,key=C.get)
			if C[D]>11:S[i]=D;B|={a(D,T(j,*T(7,*p))) for p in N[i]};break
print("Part 1: {:d}".format(len(B)))
print("Part 2: {:d}".format(max(sum(map(abs,a(S[p],T(7,*S[q])))) for p in S for q in S if p != q)))
