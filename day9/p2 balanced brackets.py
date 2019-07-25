a=input()
if(a[0]==")" or a[len(a)-1]=="("):
    print(False)
else:
    c=0
    d=0
    for i in range(0,len(a)):
        if(a[i]==")"):
            c+=1
        if(a[i]=="("):
            d+=1
    if(c==d):
        print(True)
    else:
        print(False)
