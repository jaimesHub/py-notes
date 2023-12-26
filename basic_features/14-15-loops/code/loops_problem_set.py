
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
# for character in word:
#     print(character)

# Write a while loop that does the same thing!
# repeat_time = 0

# while repeat_time != len(word):
#     print(word[repeat_time])
#     repeat_time += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
# even_number = 100
# while even_number <= 140:
#     print(even_number)
#     even_number += 2

# Write a for loop that does the same thing (with range())
# for even_number in range(100, 142, 2):
#     print(even_number)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
while input("input the passphrase 'sillygoose': ") != "sillygoose":
    print("enter again!")
print("Good")
