# write a function that will take a number and print all even numbers up to that number

def printeven(n):
    for x in range(n):
        if x % 2 == 0:
            print(x)

printeven(17)

#for x in range(6):
#     print(x)