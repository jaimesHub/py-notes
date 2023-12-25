player_1 = input("enter player_1's name: ")
player_2 = input("enter player_2's name: ")

current_player = player_1
remain_tooth_picks = 13

while True:
    sticks = "| " * remain_tooth_picks
    print(sticks)

    print(f"There are {remain_tooth_picks} toothpicks left")
    print(f"How many do you take, {current_player} ?")
    
    answer = int(input())
    while answer >= 4 or answer <= 0:
        print("You can only take 1, 2, or 3:")
        answer = int(input())
    
    remain_tooth_picks = remain_tooth_picks - answer
    if remain_tooth_picks <= 0:
        print(f"{current_player} win!!!")
        break

    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1

print("GAME OVER!!!")
    
