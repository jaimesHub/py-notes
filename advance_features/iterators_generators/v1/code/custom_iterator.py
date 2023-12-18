class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self
    
    def __next__(self):
        # return 1 # infinite print 1
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration
            
for item in Counter(1, 10):
    print(item)

# next() is used to iterate through an iterator
# When there are no more values to iterate through, an iterator will return a "StopIteration" error