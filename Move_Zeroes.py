n=int(input())
a=list(map(int,input().split()))
c=0;
for i in range(n):
    if(a[i]!=0):
        print(a[i],end=' ')
    else:
        c=c+1;
for i in range(c):
    print(0,end=' ')