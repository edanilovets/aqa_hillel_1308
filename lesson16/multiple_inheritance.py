class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves")


class Bird(Animal):
    def __init__(self, name, wing_span):
        Animal.__init__(self, name)
        self.wing_span = wing_span

    def fly(self):
        print(f"{self.name} flies")


class Horse(Animal):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def run(self):
        print(f"{self.name} runs")

class Pegasus(Bird, Horse):
    def __init__(self, name, wing_span, speed):
        Bird.__init__(self, name, wing_span)
        Horse.__init__(self, name, speed)

    def display(self):
        print(f"{self.name} is Pegasus")

pegasus = Pegasus("Bob", wing_span=4, speed=80)
pegasus.move()
pegasus.fly()
pegasus.run()
pegasus.display()
# MRO
print(Pegasus.mro())


