# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"
# iterable: "hi there", [1,2,3] => not an iterator
# iterator: iter("hi there"), iter([1,2,3]) => iterator, we can use next()

# How for-loop works ?
# behind the scence, inside the for-loop, whatever the iterable is (eg. [1,2,3], "hi there"), will return an iterator
# because inside the for-loop, iter() is being called on this string ("hi there") or this list ([1,2,3])
# then returns the iterator
# then for-loop keeps calling "next" on over and over til the end and raise Error

def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            # print("STOP OF ITERATOR!")
            break
        else:
            func(item)

def square(x):
    print(x*x)

# before adding "func" as a parameter
# my_for("hello")
# my_for([1,2,3,4,5,6])

## after adding "func" as a parameter
my_for("lol", print)
my_for([1,2,3,4,5], square)

