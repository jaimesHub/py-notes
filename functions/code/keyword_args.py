def get_total(price, qty=1, tax=0.02, discount=0):
    subtotal = price * qty * (1 - discount)
    print(subtotal * (1 + tax))

# no named argument
get_total(4.99, 5, 0.015, 0.2)

# named argument
get_total(price=9.75, qty=5, tax=0.01, discount=0.5)
get_total(price=9.75, discount=0.5, tax=0.01, qty=5) # order does not matter
get_total(9.75)
get_total(9.75, 2, tax=0.025)
# get_total(tax=0.025, 9.75, 2) # ERROR
# get_total() # ERROR