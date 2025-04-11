import sys

factorial = 1

try:
    number = int(input("Please enter a number: "))

    if number == 0:
        print(1)
        sys.exit()
     
    for count in range(1, number + 1):
        #print(count)
        factorial *= count
        #print(factorial)
        
    print(factorial)
    
except ValueError:
    print("There was a value error!")
