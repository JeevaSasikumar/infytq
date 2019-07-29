from itertools import permutations
a=input()
s=''
for i in range(len(a)):
    if(a[i]<="9" and a[i]>="0"):
        s+=a[i]
s=set(s)
s=list(s)
d=[]  
perm = permutations(s) 
for i in list(perm): 
    x=list(i)
    x=str(x)
    x=x.replace("[","").replace("'","").replace(",","").replace("]","").replace(" ","")
    x=int(x)
    if(x%2==0):
        d.append(x)
if(len(d)>0):
    print(max(d))
else:
    print(-1)
