##https://www.hackerrank.com/challenges/repeated-string/problem

##string='kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
##k=736778906400

##k=872514961806
##string='udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps'

##k=10
##string='aba'

import math
count=1
count_of_a = string.count('a')
print("First a occurences",count_of_a)
if(len(string)>1):
    if(k-len(string) == len(string)):
        print(2*count_of_a)
    else:
        multiplier=((k-len(string))//len(string))
        count=(count+multiplier)*count_of_a
        if(k%len(string) == 0):
            print("direct",count)
        else:
            count+=string[0:k%len(string)].count('a')
            print("inside mod",count)
            
            
else:
    if(count_of_a>0):
        print(k)
    else:
        print(count_of_a)
        
    
