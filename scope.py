# def myfunc():
#   x = 300
#   print(x)

# myfunc()

# 300

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc() 

# 300

# x = 300

# def myfunc():
#     print(x)

# myfunc()

# 300

# print(x)

# x = 300

# Traceback (most recent call last):
#   File "/workspaces/learning-python/scope.py", line 28, in <module>
#     print(x)
# NameError: name 'x' is not defined

# def myfunc():
#   x = 200
#   print(x)

# myfunc()

# print(x)

# 200
# Traceback (most recent call last):
#   File "/workspaces/learning-python/scope.py", line 43, in <module>
#     print(x)
# NameError: name 'x' is not defined

# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x) 

# 300

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)

# 200