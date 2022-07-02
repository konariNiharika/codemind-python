a=int(input())
b=int(input())
for n in range(a,b+1):
    sum=0
    temp=n
    while temp>0:
        rem=temp%10
        sum=sum*10+rem
        temp=temp//10
    if n==sum:
         print("%d " %n, end = '')