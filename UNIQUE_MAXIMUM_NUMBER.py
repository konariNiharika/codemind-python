n=int(input())
a=list(map(int,input().split()))
c=[]
m=0;
for i in range(n):
    p=0;
    for j in range(n):
        if(a[i]==a[j] and i!=j):
            p=p+1;
    if(p==0):
        c.append(a[i])
        m=m+1;
if(m!=0):
    print(max(c))
else:
    print("-1")