import sys
N=[('n' in l,list(map(int,l.split(',')[1::2])))for l in open(sys.argv[1]).read().replace('=',',').replace(".",',').splitlines()]
o=lambda i,j:[i,j]if i<=j else[]
def S(N):
	C=[]
	for a,p in N:C+=[e for e in [(-q,sum((o(max(p[i],b[i]),min(p[i+1],b[i+1]))for i in [0,2,4]),[])) for q,b in C] if len(e[1])>5]+[(a,p)]*a
	return sum((1+X-x)*(1+Y-y)*(1+Z-z)*a for a,(x,X,y,Y,z,Z)in C)
print("Part 1:",S(e for e in N if all(-51<q<51 for q in e[1])))
print("Part 2:",S(N))
