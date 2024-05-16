from .node import Node

class ComplexNumber(Node):
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(
            {
                "ComplexNumber": {self.number}
            }
        )
