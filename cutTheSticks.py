# https://www.hackerrank.com/challenges/cut-the-sticks/problem

def cutTheSticks(arr):
    index=True
    temp=arr
    iterator=0
    count=0
    l=[]
    while(index and sum(x for x in temp if x != 'V')!= 0):
        min_val=min(x for x in temp if x != 'V')
        # print("final array",temp,"min_val",min_val)
        if(min_val>0):
            while(iterator<len(temp)):
                if(temp[iterator] != 'V'):
                    if(temp[iterator]-min_val > 0):
                        temp[iterator]=temp[iterator]-min_val
                        # print("array",temp)
                        count+=1
                    else:
                        temp[iterator]='V'
                        # print("remove",temp)
                        count+=1
                iterator+=1
            # print("COUNT",count)
            l.append(count)
            count=0
            iterator=0
    return l