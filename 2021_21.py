import sys
a,b=map(int,open(sys.argv[1]).read()[28::30])
N=[a,b];S=[0,0];r=i=0;D=1
while max(S)<1000:p=r%2;r+=1;N[p]+=3*D+3;S[p]+=N[p]%10 or 10;D+=3
r*=3*min(S)
M=[1,3,6,7,6,3,1]
g=lambda Z,i:sum(v for _,k,v in Z if(k>20)^i)
def f(S,W,i):
	Z=[(p+o+3,s+((p+o+3)%10 or 10),n*M[o])for o in range(7) for p,s,n in S[i]]
	return (W[i]+g(Z,0)*g(S[i-1],1),[k for k in Z if k[1]<21])
S=[[(a,0,1)],[(b,0,1)]];W=[0,0]
while S[0]:W[i],S[i]=f(S,W,i);i^=1
for i in [0,1]:print("Part",str(i+1)+":",[r,max(W)][i])
