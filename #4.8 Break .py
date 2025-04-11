#loops 10 times
for x in range(10):

    #asks for a number
    number = int(input("Enter a positive number"))

    #will "break" out of the loop and proceed with the rest of the program.
    if number < 0:
        break

    #will print at the end of each iteration
    print("This is inside of the for loop")

#will print once the loop has ended normally or "break" was executed
print("This is outside of the for loop")
