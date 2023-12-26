import random

roll_1 = random.randint(1, 6)
roll_2 = random.randint(1, 6)

roll_count = 1

while roll_1 != 1 or roll_2 != 1:
    print(roll_1, roll_2)
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)

    roll_count += 1

print(roll_1, roll_2)
print("YAY SNAKE EYES!!!")
print(f"it took {roll_count} rolls")