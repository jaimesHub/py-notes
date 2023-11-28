# for letter in "supercalifragilisticexpialidocious":
#     if letter == "c":
#         break
#     print(letter)

# message = input("say hi: ")
# while True:
#     if message == "hi":
#         break
#     message = input("please say hi: ")
# print("FINALLY! THANKS FOR SAYING HI!")

for letter in "supercalifragilisticexpialidocious":
    if letter in "ueoai":
        continue
    print(letter)