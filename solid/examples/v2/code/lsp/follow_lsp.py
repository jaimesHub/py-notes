class Bird:
    def eat(self):
        print("Eating...")

class FlyingBird:
    def fly(self):
        print('Flying...')

class Eagle(FlyingBird):
    def dive(self):
        print('Diving...')

class Penguin(Bird):
    def eat(self):
        print("Penguin is eating...")

if __name__ == "__main__":
    # bird = Bird()
    # bird.fly()

    eagle = Eagle()
    eagle.fly()
    eagle.dive()