import random

lst = [['a','a'],['b','b'],['c','c'],['d','d'],['e','e']]
sec_lst = []

for i in range(len(lst)):
    sec_lst.append(lst[i][1])
    
random.shuffle(sec_lst)

def check(a,b):
    print(a,b)
    if a == b:
        return True
    else:
        return False
def inpt():
    for i in range(5):
        s = int(input('some text'))
        if s == 1:
            return True
        else:
            return False
        
def res(c,d):
    for i in range(len(c)):
        r = check(c[i][0],d[i])
        f = inpt()
        print (r)
        print (f)
        if f == r:
            print('You are right')
        else:
            print('You are wrong')
       

                
    
print( lst, sec_lst)    
res(lst,sec_lst)
#print( lst, sec_lst)
