import sys

lines = open(sys.argv[1]).readlines()

j = [ list(map(int, x.replace("->",",").split(","))) for x in lines ]
l = [[a,b,c-a,d-b] for a,b,c,d in j]

m = range(max(max(j,key=max))+1)
n = { (x,y):0 for x in m for y in m }

def r(l,c,s):
	for a,b,c,d in l:
		m = abs(c or d)
		v = [[i*c//m,i*d//m] for i in range(m+1) if s ^ (0 in [c,d])]
		for x,y in v:
			n[(a+x,b+y)] += 1
	return sum([n[k]>1 for k in n])

print("Part 1: {:d}".format(r(l,n,0)))
print("Part 2: {:d}".format(r(l,n,1)))
