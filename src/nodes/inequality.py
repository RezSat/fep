from .node import Node

class Inequality(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return str({
            "Inequality": self.op,
            "Left": self.left,
            "Right": self.right
        })
