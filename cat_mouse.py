##https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

##x,y,z=1,3,2
##x,y,z=1,2,3
##x,y,z=85,66,80

a,b=0,0
a=abs(x-z)
b=abs(y-z)
if(a<b):
    print("cat A")
elif(a>b):
    print("cat B")
else:
    print("mouse C")
