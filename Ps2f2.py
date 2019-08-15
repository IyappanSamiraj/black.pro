n,m=map(int,input().split())
num=list(map(int,input().split()))
sum=0
sub=0
add=0
for i in range(m):
    u,v=map(int,input().split())
    for j in range(u-1,v):
        sum=sum+num[j]
    sub=sum-add
    add=sub+add
    print(sub)
