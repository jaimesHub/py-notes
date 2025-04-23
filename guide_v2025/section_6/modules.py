# import time
#
# print(time.sleep(2))
# print("hello world")

# import module_greetings

# alias
# import module_greetings as g
#
# g.greet('Bob')
# print(g.AUTHOR)

# import specific def / var
# from module_greetings import  greet
# greet('Jack')

# import all elements in a module
from module_greetings import  *
greet('Alice')
print(AUTHOR)
print(VERSION)