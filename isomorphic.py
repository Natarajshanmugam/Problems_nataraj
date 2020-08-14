a=list(map(str,input().split()))
b="".join(list(set(a[0])))
##print(b)
l1=[]
l2=[]
f=0
if(len(a[0])==len(a[1])):
    for i in range(len(b)):
        for j in range(0,len(a[0])):
            if(b[i]==a[0][j]):
                l1.append(j)
##                print(a[0][j])
##        print(l1)
        c=l1[0]
        d=a[1][c]
        for i in l1:
            if(a[1][i] not in l2):
                continue
            else:
                f=1
                break
        l2.append(d)
        if(f==1):
            break
        else:
            l1=[]
            continue
    if(f==1):
        print("no")
    else:
        print("yes")

else:
    print("no")
