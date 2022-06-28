n=int(input())
a=list(map(int,input().split()))
h=int(input())
for i in range(len(a)):
    c=0;
    if(a[i]==h):
        c=c+1;
        print(i)
        break;
if(c==0):
    print(-1);