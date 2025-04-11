#this is our main function where the program will begin
def main():

    #call the sayHello function, which returns a string, then store the string in "message"
    message = sayHello()

    #print the message
    print(message)

    #shows we are back in main
    print("We are back in the main function")

#our sayHello function that will execute once called
def sayHello():
    
    #gives back the string, "Hello there!"
    return("Hello there!")

main()
