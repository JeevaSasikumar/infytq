a=list(map(int,input().split()))
c=0
for i in range(0,len(a)-2):
    if(a[i]==1 and a[i+1]==2 and a[i+2]==3):
        print(True)
        c=1
        break
if(c==0):
    print(False)
        

