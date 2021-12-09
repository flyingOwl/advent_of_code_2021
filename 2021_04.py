import sys

lines = open(sys.argv[1]).readlines()

n = list(map(int,lines[0].split(',')))
b = {}
for i in range(len(lines) // 6):
	b[i] = [[int(x) for x in lines[2+i*6+j].split()] for j in range(5)]
	b[i] += zip(*b[i])

def s(b):
	m = min(next(i for i in range(len(n)+1) if all(map(n[:i].count,r))) for r in b)
	u = sum(set(a for B in b for a in B)-set(n[:m]))
	return m,u*n[m-1]

z = [s(b[i]) for i in b]
print("Part 1: {:d}".format(min(z)[1]))
print("Part 2: {:d}".format(max(z)[1]))
