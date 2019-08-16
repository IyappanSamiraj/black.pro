n=int(input())
a=[]
for i in range(n):
    m=list(map(int,input().split()))
    for j in range(len(m)):
        a.append(m[j])
a1=sorted(a)
print(*a1)
