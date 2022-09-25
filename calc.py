from test_1 import sum
from test_2 import multiply
from test_3 import divide


class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return sum(self.a, self.b)

    def mul(self):
        return multiply(self.a, self.b)

    def div(self):
        return divide(self.a, self.b)
