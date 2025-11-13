list=[23,34,"ram","riya",45]
string=[]
num=[]
for i in list:
    if(i==int(i)):
        num+=[i]
    else:
        string+=[i]
print(num)
print(string)

