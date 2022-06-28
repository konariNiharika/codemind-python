n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    c=1
    for j in range(n):
        if(a[i]==a[j] and i!=j):
            c=c+1;
    if(c>n/2):
        print(a[i])
        break