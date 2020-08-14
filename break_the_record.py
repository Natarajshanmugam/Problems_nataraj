a = int(input())
b = list(map(int,input().split()))[:a]
max_1=[]
min_1=[]
max_1.append(b[0])
min_1.append(b[0])
for i in range(len(b)):
    if(b[i]>max_1[len(max_1)-1]):
        max_1.append(b[i])
        print("max",max_1)
    elif(b[i]<min_1[len(min_1)-1]):
        min_1.append(b[i])
        print("min",min_1)
    
print(len(max_1)-1,len(min_1)-1)
