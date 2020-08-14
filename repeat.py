a=list(input())
b=a.copy()
c=''
l=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            l.append(a[i])
            break
print(l)
for i in range(len(b)):
    if b[i] in l:
        a.remove(b[i])
        print(a)
for i in a:
    c=c+i
print(c)
