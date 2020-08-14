a = list(map(int,input().split()))
b = a[0]+a[1]
c = a[2]+a[3]
count=0
print(b," ",c)
if a[2]>a[0] and a[3]>a[1]:
    print("NO")

else:
    for i in range(100000):
        if b==c:
            print(b," ",c,"YES")
            break
        else:
            b +=a[1]
            c +=a[3]
        count+=1
        if count==100000:
            print("NO")
  
