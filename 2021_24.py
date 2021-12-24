import sys,random
P=[s.strip().splitlines() for s in open(sys.argv[1]).read().split("inp w") if s]
A=[0]*14;B=[0]*14;S=[]

for i,p in enumerate(P):
	if '1' in p[3]:S+=[(i,int(p[14].split()[2]))]
	else:
		j,y=S.pop()
		d=y+int(p[4].split()[2])
		if d<0:j,i,d=i,j,-d
		A[j]=9-d;A[i]=9
		B[j]=1;B[i]=1+d
print("Part 1: "+''.join(map(str,A)))
print("Part 2: "+''.join(map(str,B)))
