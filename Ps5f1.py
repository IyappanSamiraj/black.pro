a,b,c=map(int,input().split())
sum=b+c
while(a!=0 and a>0):
	a=a-sum
if(a==0):
	print('YES')
else:
	print('NO')
