num=7
u=int(input("enter the number:"))
while True:
    if u<num:
        print("Too low!Try again")
        break
    elif u>num:
        print("Too high!Try again")
        break
    else:
        print("Correct")
        break
    
