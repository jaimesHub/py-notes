class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    # pass
    def do_something(self):
        print("Method Defined In: B")
        super().do_something()

class C(A):
    # pass
    def do_something(self):
        print("Method Defined In: C")

class D(C, B):
    # pass
    def do_something(self):
        print("Method Defined In: D")
        super().do_something()

# print(D.__mro__)
# print(D.mro())
# help(D)
thing = D()
thing.do_something()

# D,B,C,A,Object