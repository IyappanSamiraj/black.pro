n,k=map(int,input().split())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i]+a[j]==k):
            sum=sum+1
if sum>0:
    print('yes')
else:
    print('no')
            
