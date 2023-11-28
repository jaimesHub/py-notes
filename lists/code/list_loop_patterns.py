lando_2021_results = [2, 4, 1, 4, 7, 4, 3, 10, 9, 6, 3, 3, 7, 2, 77, 11, 8, 4, 6, 7, 3]

# total = 0
# for num in lando_2021_results:
#     total += num
# avg = total / len(lando_2021_results)
# print(total, avg)

def average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

############

min = lando_2021_results[0]
for num in lando_2021_results:
    if num < min:
        min = num
print(min)