a = list(map(int,input().split()))
b = list(map(int,input().split()))[:a[0]]
print(b)
##s=''
##l=[]
c=0
b.sort()
for i in range(len(b)):
    for j in range(i+1,len(b)-1):
        for k in range(j+1,len(b)):
            if (b[i]*a[1] == b[j] and b[j]*a[1] == b[k]):
                c+=1
##                s = s+str(b[i])+str(b[j])+str(b[k])
##                l.append(s)
##                print(s)
##                s=''
print(c)
