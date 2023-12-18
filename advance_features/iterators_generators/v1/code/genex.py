def nums():
    for num in range(1, 10):
        yield num

# In [1]: def nums():
#    ...:     for num in range(1, 10):
#    ...:         yield num
#    ...: 

# In [2]: g = nums()

# In [3]: next(g)
# Out[3]: 1

# In [4]: next(g)
# Out[4]: 2

# In [5]: next(g)
# Out[5]: 3

# In [6]: next(g)
# Out[6]: 4

# In [7]: g = (num for num in range(1,10))

# In [8]: g
# generator expression
# Out[8]: <generator object <genexpr> at 0x10608fb80>

# In [9]: g = nums()

# In [10]: g
# generator function
# Out[10]: <generator object nums at 0x1060e3e00>