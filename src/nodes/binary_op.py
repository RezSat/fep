from .node import Node

class BinaryOperation(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = self.op
        self.right = self.right
    
    def __repr__(self):
        return {
            "BinaryOperation": self.op,
            "Left": self.left,
            "Right": self.right
        }

    def __str__(self):
        return str(self.__repr__())

class Add(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "+", right)

class Subtract(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "-", right)

class Multiply(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "*", right)

class Divide(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "/", right)

class Power(BinaryOperation):
    def __init__(self, base, index):
        super().__init__(base, "^", index)


