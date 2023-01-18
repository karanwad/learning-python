#write a function that will take a list as an argument and print out each item in it as long as it's an even number

def printitem(numbers):
    for x in numbers:
        if x % 2 == 0:
            print(x)

list = [5, 10, 3, 9, 20, 4, 22]

printitem(list)