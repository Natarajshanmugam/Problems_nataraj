a = list(map(int,input().split()))
b = list(map(int,input().split()))[:a[0]]
c=0
print(a)
print(b)
for i in range(len(b)-1):
    for j in range(i+1,len(b)):
        if (abs(b[i]-b[j]) == a[1]):
            c+=1
print(c)
