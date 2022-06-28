n=int(input())
a=list(map(int,input().split()))
m=int(input())
p=0
for i in range(len(a)):
    if(a[i]>p):
        p=a[i];
for i in range(len(a)):
    if(a[i]+m>=p):
        print("True",end=' ')
    else:
        print("False",end=' ')