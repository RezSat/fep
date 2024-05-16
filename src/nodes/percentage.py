from .node import Node

class Percentage(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str({
            "Percentage": self.value
        })
