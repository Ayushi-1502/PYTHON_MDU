list=[1,5,22,9,14,3,4,88,7]
even=[]
odd=[]
for item in list:
    if item%2==0:
        even.append(item)

    else:
        odd.append(item)
print(even)
print(odd)
