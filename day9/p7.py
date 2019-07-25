a=list(map(int,input().split()))
c=str(a[0])
s=a[0]
for i in range(0,len(c)):
    s*=int(c[i])
if(s==a[1]):
    print(True)
else:
    print(False)
