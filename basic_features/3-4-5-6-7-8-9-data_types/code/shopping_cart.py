# Prints out a “banner” to welcome users to our shop
print("WELCOME TO OUR USELESS STORE!")
print("*****************************")
# Asks the user for the name of the item they are buying
item_name = input("what item are you purchasing?")
# Asks the user for the price of that item
price = input(f"what is the price of {item_name}?")
# Asks the user for the quantity they are purchasing
quantity = input(f"how many {item_name} are you buying?")
print()
# Prints out a message that includes their subtotal (quantity 𝚡 price)
print(f"Added {quantity} {item_name}(s) to shopping cart")
print(f"Subtotal: ${float(quantity) * float(price)}")