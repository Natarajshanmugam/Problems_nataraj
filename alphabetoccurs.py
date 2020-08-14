a=input()
l=[]
s1=''
s2=''
f=0
for i in range(0,len(a)-1):
    b=a[i]+a[i+1]
    c=a[0:i]+a[i+2:len(a)]
    print(i,b,c)
    if(int(b)<=26):
        s1=s1+chr(96+int(b))
        for j in c:
            s1=s1+chr(96+int(j))
        l.append(s1)
        print(s1)
        s1=''
        if(int(i)%2==0):
            if(len(a)%2==0):
                s2=s2+chr(96+int(b))
                print(b,s2)
            else:
                s2=s2+chr(96+int(b))
                f=1
                print(b,s2)
if(f==1):
    s2=s2+chr(96+int(a[len(a)-1]))
    if s2 not in l:
        l.append(s2)
        print(s2,"f")
len1=len(a)//2
if(len1==len(s2)):
    l.append(s2)
print(l)
print(len(l)+1)
    
