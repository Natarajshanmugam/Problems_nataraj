a = int(input())
b = int(input())
if(b==1 or a==b):
    print("0")
else:
    if(a%2==0):
        if(a//2>=b):
            for i in range(2,a,2):
                print(i)
        else:
            for i in range(a-1,1,-2):
                print(i)
    else:
        
                
##    for i in range(2,a-1,2):
##        print(i)
