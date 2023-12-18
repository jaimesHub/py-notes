# What if n = 1
# What if n = 10
# What if n = 100
# What if n = 1000
# What if n = 10000
# What if n = 100000
# What if n = 1000000
# What if n = 10000000 
# => we need to generators, yield
# https://docs.python.org/3/howto/functional.html#generators
# https://youtu.be/nLRL_NcnK-4?si=JMV5HevLVYL_QMJl&t=56217
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print("🐑" * s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

# that is generator function
def sheep(n):
    for i in range(n):
        yield "🐑" * i # return 1 value at a time

if __name__ == "__main__":
    main()