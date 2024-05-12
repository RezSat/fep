from .node import Node

class Symbol(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str({
            "Symbol": self.value
        })
