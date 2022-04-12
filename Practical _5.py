word = input("Enter your string :   \n")
l = list(word)
print("\nSwap is : ")
for x in l:
    if(x.islower()):
        print(x.upper(), end="")
    elif(x.isupper()):
        print(x.lower(), end="")
    elif(x.isnumeric):
        print(x, end="")
    elif(not (x.isalnum())):
        print(x, end="")