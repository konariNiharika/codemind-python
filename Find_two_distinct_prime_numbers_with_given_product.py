n=int(input())
c=0
for i in range(1,n+1):
    for j in range(2,n+1):
        for k in range(2,n+1):
            if(i%j!=0 and i%k!=0):
                if(j*k==n):
                    p=j;
                    q=k;
                    c+=1
                    break;
if(c!=0):
    print(q,p)
else:
    print("-1")