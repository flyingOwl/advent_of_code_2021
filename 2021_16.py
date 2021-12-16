import sys
i=int
m=lambda x:x[0]*m(x[1:])if x else 1
s=lambda x:s(x[:-1])<<4|x[-1]if x else 0
def p(N):
	V=i(N[:3],2);T=i(N[3:6],2);l=T==4;b,W=i(N[6])+l,[];C=c=[22-b*4,6][l];v=i(N[7-7*l:C],2)
	while[c-C,len(W),0][b]<v:
		z,w,d=(0,i(N[c+1:c+5],2),5)if l else p(N[c:])
		v*=(1^l)|i(N[c]);W+=[w];V+=z;c+=d
	f=[sum,m,min,max,s,i.__gt__,i.__lt__,i.__eq__][T];return(V,i(f(*W)if T>4 else f(W)),c)
for a in[0,1]:print("Part",a+1,":",p(bin(i(n:=open(sys.argv[1]).read()[:-1],16))[2:].zfill(len(n)*4))[a])
