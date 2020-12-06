from random import random

class EvenDistribution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random()
