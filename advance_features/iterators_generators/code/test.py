import time

# expression
gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_stop = time.time() - gen_start_time

# list comprehension
list_start_time = time.time()
print(sum([n for n in range(10000000)]))
list_stop = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) took: {gen_stop}")
print(f"sum([n for n in range(10000000)]) took: {list_stop}")

