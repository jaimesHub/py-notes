# check a number is an even or odd number
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False # unnecessary return
    
# how can we have multiple return statements
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# improve code
def is_even(num):
    return num % 2 == 0

# slugify a string
def slugify(phrase):
    return phrase.lower().strip().replace(" ", "-")

# res = slugify("hello world I LOVE YOU")
# print(res) # hello-world-i-love-you

# res2 = slugify("   Hello world I LOVE YOU    ")
# print(res2) # hello-world-i-love-you

# count how many vowel in a string
# count_vowels

def count_vowels(word):
    count = 0
    for character in word:
        if character in "ueoai":
            count += 1
    return count

# print(count_vowels("hello world"))
# print(count_vowels("pineapple"))
# print(count_vowels("lll"))
    
