from contextlib import contextmanager

@contextmanager
def colored_output(color):
    print("\033[%sm" % color, end="")  # lines before the yield associated with __enter__ method
    yield
    print("\033[0m", end="")  # lines after the yield associated with __exit__ method


print("Hello, World!")
with colored_output(31):
    print("Now in color!")
print("So cool.")