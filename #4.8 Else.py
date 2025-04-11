#loop 3 times
for n in range(3):

    #if n does equal 5, which it won't, it will break out of the loop
    if n == 5:
        print("Breaking out of loop")
        break

    #prints n after each iteration
    print(n)

#if "break" does NOT execute, this else block will be executed
#if "break" DOES execute, the else block will be skipped
else:
    print(f'After the loop, n is {n}')

#indicates outside of loop
print("Hello!")
