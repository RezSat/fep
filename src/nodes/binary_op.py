from .node import Node

class BinaryOperation(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return str({
            "BinaryOperation": self.op,
            "Left": self.left,
            "Right": self.right
        })


class Add(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left=left, op="+", right=right)

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


