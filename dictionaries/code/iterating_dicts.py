test_scores = {
    "Marsha": 78,
    "Baker": 69,
    "Rosa": 92,
    "Leif": 97,
    "Peng": 61,
    "Juan": 73,
    "Esteban": 84,
    "Amir": 91,
    "Sakura": 99
}

# for student in test_scores.keys():
#     print(student)

# for score in test_scores.values():
#     print(score)

# total = 0
# for score in test_scores.values():
#     total += score
# print(total / len(test_scores))

# for key in test_scores.keys():
#     print(test_scores[key])

# for item in test_scores.items():
#     print(item)

# for k,v in test_scores.items():
#     print(k, v)

max_score = 0
best_student = ""

for student, score in test_scores.items():
    if score > max_score:
        max_score = score
        best_student = student

print(f"Highest score was {max_score} by {student}")