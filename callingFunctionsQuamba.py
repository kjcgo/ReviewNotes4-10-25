#this is our main file
def main():

    #we are calling our sayHello function, meaning the computer will start executing statements 
    #in that function
    sayHello()

    #the program will return to the main function
    print("We are back in the main function")

def sayHello():

    #the computer will print these statements when the function is called
    print("Hello There!")
    print("This is inside the sayHello function.")

    #once these statements have been executed, the program "returns" to the main function
main()
