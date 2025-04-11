#initialize n
n = 0

#keep going until n < 10 is false
while n < 10:    

    #add one to n
    n += 1

    #if n is divisible by 3, go back to the start of the loop
    if n % 3 == 0:
        continue

    #will print at the end of each iteration, is skipped if "continue" executes
    print(n)

#will print when the loop is complete
print("We are done with the loop")

