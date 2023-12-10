class Bird:
    """This class violates the LSP
    Because it wants to ensure that you do not model your data in the wrong way
    In here, we pick Bird as a base class, but Penguin can not fly
    """
    def fly(self):
        print('Flying...')

class Eagle(Bird):
    def dive(self):
        print('Diving...')

class Penguin(Bird):
    """Problem: Can't fly -> We had a wrong base class (Bird)
    """

if __name__ == "__main__":
    # bird = Bird()
    # bird.fly()

    eagle = Eagle()
    eagle.fly()