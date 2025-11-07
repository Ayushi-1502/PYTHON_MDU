a=int(input("Enter the marks of first subject:"))
b=int(input("Enter the marks of second subject:"))
c=int(input("Enter the marks of third subject:"))
d=int(input("Enter the marks of fourth subject:"))
e=int(input("Enter the marks of five subject:"))
total=a+b+c+d+e
print(total)
avg=a+b+c+d+e/5
print(avg)
if(avg>=90):
    print("Grade A")
elif(avg>=80 and avg<=89):
    print("Grade B")
elif(avg>=70 and avg<=79):
    print("Grade C")
else:
    print("Grade D")
    