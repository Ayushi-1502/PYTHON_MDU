list=[]
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
num4=int(input("enter the fourth number:"))
num5=int(input("enter the fiveth number:"))
list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
print(list)
sum=0
for i in list:
    if i%2!=0:
        sum=0+i
print(sum)