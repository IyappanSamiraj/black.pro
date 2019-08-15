n,m=map(int,input().split())
num=list(map(int,input().split()))
for i in range(m):
    u,v=map(int,input().split())
    sum=[]
    for j in range(u-1,v):
        sum.append(num[j])
    print(min(sum))
