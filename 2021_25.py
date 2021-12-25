import sys
P=[[{'.':0,'>':1,'v':2}[c] for c in s] for s in open(sys.argv[1]).read().splitlines()]
E=enumerate
def g(P,X,Y):
	s=0;Q=[list(l) for l in P]
	for y,l in E(P):
		for x,m in E(l):
			if m==0 and P[y-Y][x-X]==Y+1:Q[y][x]=Y+1;Q[y-Y][x-X]=0;s=1
	return (Q,s)
S=1;a=0
while S:Q,s=g(P,1,0);P,t=g(Q,0,1);S=s+t;a+=1
print("Part 1:",a)
