# Write a Python function that takes in 3 numbers and returns the greatest one 

def greatest(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z

greatest(5, 55, 3)





