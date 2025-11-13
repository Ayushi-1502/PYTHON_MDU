sen=input("Wirte a sentence:")
Vowels="aeiouAEIOU"
v_count=0
c_count=0
for i in sen:
    print(i)
    if i in Vowels:
        v_count+=1
    else:
        c_count+=1
print("The number of vowels:",v_count)
print("The number of consonants:",c_count)
