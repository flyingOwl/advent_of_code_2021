import sys
e=enumerate
N={(x,y):int(v) for y,l in e(open(sys.argv[1]).read().split('\n')) for x,v in e(l)}
def a(N):
	Z=max(N)
	O,V={Z},{Z:0}
	while any(O):
		x,y=b=min(O,key=V.get)
		f = V[b]+N[b]
		for p in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
			if p in N and f<V.get(p,f+1):
				V[p]=f
				O|={p}
		O-={b}
	return V[0,0]
R,X,Y=range(5),*max(N)
O = {(x+a*(X+1),y+b*(Y+1)):(N[x,y]+a+b-1)%9+1 for x,y in N for a in R for b in R}
print("Part 1: {:d}".format(a(N)))
print("Part 2: {:d}".format(a(O)))
