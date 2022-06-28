n=int(input())
for i in range(1,n):
    if(i*i==n):
        break;
if(n==i*i):
    print("True")
else:
    print("False")