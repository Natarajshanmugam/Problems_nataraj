from itertools import combinations
a = list(map(int,input().split()))
b = list(map(int,input().split()))[:a[0]]
print(b)
l=[]
f=0


for i in range(50,1,-1):
    perm = list(combinations(b,i))
    for i in range(len(perm)):
        print(perm[i])
        for j in range(len(perm[i])):
            for k in range(j+1,len(perm[i])):
##                print(j," ",k)
##                print(perm[i][j]," ",perm[i][k])
                if((perm[i][j]+perm[i][k])%a[1]!=0):
                    print(perm[i][j],"DIVIDE",perm[i][k])
                    f = 0
                    continue
                else:
                    f = 1
                    break
            if(f==1):
                break
        if(f==0):
            print("HELLO",len(perm[i]))
            break
        l=[]
    if(f==0):
        break
    else:
        print("1")
