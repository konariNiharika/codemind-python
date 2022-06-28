n=int(input())
a=list(map(int,input().split()))
m=0;
for i in range(len(a)):
    c=0;
    for j in range(len(a)):
        if(a[i]==a[j] and i!=j):
            c=c+1;
    if(c==0):
        print(a[i],end=' ')
        m=m+1;
if(m==0):
    print(-1)