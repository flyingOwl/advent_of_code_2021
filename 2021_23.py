import sys
N=list(filter(str.isalnum,open(sys.argv[1]).read()))
S={'H':[0]*11};L="ABCD";b=bool;Z=enumerate
for c in L:S[c]=N[ord(c)-65::4]

C=lambda S:{c:list(S[c]) for c in S}
P=lambda k:2*(ord(k)-64)
g=lambda S,i,j:1^any(S['H'][i:j:[-1,1][j>i]])

def f(S,W=1e5,V={},w=0):
	if min(W,V.get(str(S),W))<=w:return W
	V[str(S)]=w
	d=[(i,c,x) for i,c in Z(S['H']) if i not in [2,4,6,8] for x in [L,[c]][b(c)] if any(e not in [0,x] for e in S[x])^b(c) and g(S,*[i,P(x)][::[1,-1][b(c)]])]
	for i,c,e in d:
		j,k=(len(S[e])-S[e][::-1].index(0)-1,e) if c else next(z for z in Z(S[e]) if z[1])
		s=C(S);s['H'][i],s[e][j]=s[e][j],s['H'][i]
		v=(abs(i-P(e))+1+j)*10**(ord(k)-65)
		W=min(W,f(s,W,V,w+v))
	return [W,w][all(e==c for c in L for e in S[c])]

print("Part 1:",f(S))
S['A'][1:]=['D','D',N[4]]
S['B'][1:]=['C','B',N[5]]
S['C'][1:]=['B','A',N[6]]
S['D'][1:]=['A','C',N[7]]
print("Part 2:",f(S))
