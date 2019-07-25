a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    if(i==4):
        break
    if(a[i]==9):
        print(True)
        c=1
        break
if(c==0):
    print(False)
