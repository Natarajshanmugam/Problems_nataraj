import numpy
d=[]
t_matrix=[]
for i in range(0,3):
    a=list(map(int,input().split()))
    d.append(a)
print(d)
for i in range(3):
    a=[]
    for j in range(3):
        a.append(d[j][i])
    t_matrix.append(a)
##t_matrix = list(numpy.transpose(d))
print("normal",t_matrix)
result = 0
m_sum=0
##for i in range(3):
##    for j in range(3):
##        if i==j:
##            m_sum += d[i][i]
##print(m_sum)
m_sum = d[0][2] + d[1][1] + d[2][0]
for i in range(3):
    for j in range(3):
        if ((i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0)):
            continue
        else:
            s = sum(d[i])
##            print(s)
            if s<m_sum:
                diff = m_sum-s
                if(d[i][j]+diff <=9):
                    if(sum(t_matrix[j])==m_sum):
                        print("+EQUAL",sum(t_matrix[j]))
                        continue
                    else:
                        print("+",sum(t_matrix[j]))
                        d[i][j] = d[i][j]+diff
                        t_matrix[j][i] = d[i][j]
                        result+=diff
                        print(d)
                        print(t_matrix)
            elif(s>m_sum):
                diff = s-m_sum
                if(d[i][j]-diff <=9):
                    if(sum(t_matrix[j])==m_sum):
                        print("-EQUAL",sum(t_matrix[j]))
                        continue
                    else:
                        print("-",sum(t_matrix[j]))
                        d[i][j] = d[i][j]-diff
                        t_matrix[j][i] = d[i][j]
                        result+=diff
                        print(d)
                        print(t_matrix)
            else:
                continue
print("Final",d)
print("Result",result)
