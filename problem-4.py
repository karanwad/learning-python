# Write a Python function that takes in 3 numbers and returns the greatest one 


x = input('give me a number')
y = input('give me a second number')
z = input('give me a third number')

def greatest():
    if x > y and x > z:
        print(x)
    if y > x and y > z:
        print (y)
    if z > x and z > y:
        print (z)

greatest()

# print(x, y, z)

# l = [x, y, z]

# print(max(l))

