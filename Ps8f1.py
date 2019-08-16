n,m=map(int,input().split())
num=list(map(int,input().split()))
for i in range(m):
    u,v=map(int,input().split())
    if(u==v):
        print(num[u-1])
    else:
        u=u-1
        v=v-1
        if(num[u]>num[v]):
            if(num[v]==1):
                f=num[v]%num[u]
                print(f)
            else:
                f=num[u]%num[v]
                print(f)
        else:
            if(num[u]==1):
                f=num[u]%num[v]
                print(f)
            else:
                f=num[v]%num[u]
                print(f)
    
    
    

    
