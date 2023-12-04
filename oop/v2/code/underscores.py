# _name: private attributes/methods
# __name: name mangling
# __name__: Dunder methods

class Person:
    def __init__(self) -> None:
        self.name = "Tony"
        self._secret = "hi!" # just a convention
        self.__msg = "I like turtles!"

p = Person()
p.name
p._secret
# error
p.__msg
# fix
p._Person__msg

print(dir(p)) # there is no "__msg"