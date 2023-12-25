mood = "happy"

if mood == "happy":
    # Error: unexpected indent
# print("I'm happy you are happy")
# print(":)" * 10)

    # It works with 1 space
#  print("I'm happy you are happy")
#  print(":)" * 10)

    # Error: unexpected indent
    # print("I'm happy you are happy")
    #   print(":)" * 10)

    # It works with other result
#     print("I'm happy you are happy")
# print(":)" * 10)

    print("I'm happy you are happy")
    print(":)" * 10)
elif mood == "sad":
    print("I'm sorry that sucks :(")

    # error: invalid syntax
#  elif mood == "sad":
#     print("I'm sorry that sucks :(")

    # invalid syntax
    # else:
    # print("I don't know that mood!")

else:
    print("I don't know that mood!")