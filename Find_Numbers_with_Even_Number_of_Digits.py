n=int(input())
a=list(map(int,input().split()))
c=0;
for i in range(len(a)):
    dc=0;
    while(a[i]):
        d=a[i]%10;
        a[i]=a[i]//10;
        dc=dc+1;
    if(dc%2==0):
        c=c+1;
print(c)