import math
a = input()
a = a.replace(' ','')
print(len(a))
l=[]
s=""
sqrt_value = int(math.sqrt(len(a)))
if (sqrt_value*sqrt_value == len(a)):
    rows = sqrt_value
    cols = sqrt_value
else:
    rows = int(sqrt_value)
    cols = rows+1
print(rows," ",cols)
if (rows*cols >= len(a)):
    for i in range(0,len(a),cols):
        print(a[i:i+cols])
        l.append(a[i:i+cols])
else:
    print("dg")
    for i in range(0,len(a),cols):
        print(a[i:i+cols])
        l.append(a[i:i+cols])
print(l)
for i in range(cols):
    for j in range(len(l)):
        try:
            print(l[j][i])
            s = s + l[j][i]
        except Exception as e:
            pass
    s = s+" "
    print(s)
print(s)
