# def outer():
#     global animal
#     animal = "Spider Crab"
# outer()

# print(animal)
# # Spider Crab

# score = 100

# def double_score():
#     score = score * 2

# double_score()
# # error: local variable 'score' referenced before assignment

score = 100

def double_score():
    global score
    score = score * 2

double_score()
print(score)