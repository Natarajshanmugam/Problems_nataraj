a=list(map(str,input().split()))
l=[]
for i in range(len(a[0])):
    for j in range(i+1,len(a[0])):
        if(a[0][i] == a[0][j]):
            if(a[1][i] == a[1][j]):
                if a[1][i] not in l:
                    l.append(a[1][i])
                    continue
                else:
                    f=1
                    break
            else:
                f=1
                break
        else:
            if a[1][i] not in l:
                l.append(a[1][i])
            else:
                f=1
                break
                    
            
