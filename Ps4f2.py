n,m=map(int,input().split())
num=list(map(int,input().split()))
sum=0
for i in range(m):
    u,v=map(int,input().split())
    for j in range(u-1,v):
        sum=num[j]^sum
    print(sum)
    sub=sum
    sum=sub-sum
    
    

    
