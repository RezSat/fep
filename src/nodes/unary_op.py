from .node import Node

class UnaryOperation(Node):
    def __init__(self, op, value):
        self.op = op
        self.value = value

    def __repr__(self):
        return str({
            "UnaryOperation": self.op,
            "Value": self.value
        })

class Positive(UnaryOperation):
    def __init__(self, value):
        super().__init__(op="+", value=value)

class Negative(UnaryOperation):
    def __init__(self, value):
        super().__init__(op="-", value=value)
