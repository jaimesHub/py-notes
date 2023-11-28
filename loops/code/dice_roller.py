import random

while True:
    number_of_dices = int(input("How many dice are we rolling? "))
    sides = int(input("How many sides on each die? "))

    if not (number_of_dices in range(1, 21) and sides in range(1, 21)):
        print("Invalid input! Please input again!")
        continue

    result = "|"
    
    for dice_nth in range(number_of_dices):
        result += f"{random.randint(1, sides)}|"
    
    print(result)

    answer = input("Roll again? ('q' to quit) ")

    if answer == "q":
        break