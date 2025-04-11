n= 0
for x in range(10):
    number = int(input("Enter a positive number"))

    if number < 0:
        break
    print("This is inside of the for loop")
    
print("This is outside of the for loop")
