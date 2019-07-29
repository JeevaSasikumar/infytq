m=int(input())
a=list(map(int,input().split()))
n=len(a)
for i in range(1,m):
    b=list(map(int,input().split()))
    for j in range(0,m):
        a.append(b[j])
c=m*n
d=[]
print(a)
for i in range(0,c):
    if(i%n<=n-4):
        if(a[i]==a[i+1] and a[i+1]==a[i+2] and a[i+1]==a[i+2]):
            d.append(a[i])
for i in range(0,c):
    if(i<2*n):
        if(a[i]==a[i+n] and a[i+n]==a[i+2*n] and a[i]==a[i+3*n]):
            d.append(a[i])
for i in range(0,c):
    if(i<2*n and i%n<=n-4):
        if(a[i]==a[i+(n+1)] and a[i]==a[i+(2*(n+1))] and a[i]==a[i+(3*(n+1))]):
            d.append(a[i])
for i in range(0,c):
    if(i<2*n and i%n>2):
        if(a[i]==a[i+n-1] and a[i]==a[i+(2*(n-1))] and a[i]==a[i+(3*(n-1))]):
            d.append(a[i])
        
print(min(d))
