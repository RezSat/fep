from .node import Node

class Equation(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return str(
            { "Equation": {
                "Left": self.left,
                "Right": self.right
            }
            }
        )
