# def add_thrice(val, lst=[]):
#     lst.append(val)
#     lst.append(val)
#     lst.append(val)

#     return lst

# add_thrice(7, [1,2,3])
# add_thrice(99) 
# add_thrice(0)

# Fix
def add_thrice(val, lst=None):
    if lst is None:
        lst = []
        
    lst.append(val)
    lst.append(val)
    lst.append(val)

    return lst

add_thrice(7, [1,2,3])
add_thrice(99) 
add_thrice(0)