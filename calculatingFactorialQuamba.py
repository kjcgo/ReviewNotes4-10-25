#this import allows us to use sys.exit()
import sys

#set factorial equal to 1
factorial = 1

#try to get input from the user
try:

    #ask for a number
    number = int(input("Please enter a number: "))

    #if the number is 0, print 1 and end the program
    if number == 0:
        print(1)
        sys.exit()

    #if the number is not zero, loop that many times starting from one, and multiply each number together
    for count in range(1, number + 1):
        #print(count)
        factorial *= count
        #print(factorial)

    #show what the factorial is 
    print(factorial)

#will execute if the user does not provide correct input
except ValueError:
    print("There was a value error!")
