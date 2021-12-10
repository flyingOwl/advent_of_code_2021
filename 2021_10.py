import sys

L = open(sys.argv[1]).read().splitlines()

O = {'(':')','<':'>','{':'}','[':']'}
C = {')':(3,1),']':(57,2),'}':(1197,3),'>':(25137,4)}

def s(l):
	S = []
	for c in l:
		if c in O:
			S.append(O[c])
		elif S.pop() != c:
			return C[c][0],[]
	return 0,S

m = list(map(s,L))
n = sorted(sum(5**i*C[v][1] for i,v in enumerate(M[1])) for M in m if M[1])

print("Part 1: {:d}".format(sum(m[0] for m in m)))
print("Part 2: {:d}".format(n[len(n)//2]))
