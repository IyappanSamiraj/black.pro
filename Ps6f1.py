n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range (len(a)):
    for j in range (len(a)):
        for k in range(len(a)):
            if(a[i] < a[j] < a[k]):
                if(i < j < k):
                    sum=sum+1
print(sum)
