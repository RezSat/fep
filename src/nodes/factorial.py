from .node import Node

class Factorial(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str({
            "Factorial": self.value
        })
