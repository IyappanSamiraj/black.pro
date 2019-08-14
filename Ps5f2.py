n=int(input())
num=list(map(int,input().split()))
final=[]
for i in num:
    if i not in final:
        final.append(i)
m=sorted(final)
k=m[::-1]
print(*k,sep="\n")
