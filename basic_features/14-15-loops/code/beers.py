# total_bottles_of_beers = int(input("enter number: "))

# while total_bottles_of_beers > 0:
#     print(f"{total_bottles_of_beers} bottles of beer on the wall.")
#     print(f"{total_bottles_of_beers} bottles of beer." )
#     total_bottles_of_beers -= 1
#     if total_bottles_of_beers > 0:
#         print(f"Take one down, pass it around, {total_bottles_of_beers} bottles of beer on the wall")
#     else:
#         print(f"Take one down, pass it around, no more bottles of beer on the wall")
#     print("************************************************************")

for num_bottles in range(99, 0, -1):
    print(f"{num_bottles} bottles of beer on the wall.")
    print(f"{num_bottles} bottles of beer." )

    if num_bottles == 1:
        print(f"Take one down, pass it around, no more bottles of beer on the wall.")
    elif num_bottles == 2:
        print(f"Take one down, pass it around, {num_bottles - 1} bottle of beer on the wall.")
    else:
        print(f"Take one down, pass it around, {num_bottles - 1} bottles of beer on the wall.")
    
    print("************************************************************")

