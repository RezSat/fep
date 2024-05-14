from .node import Node

class Set(Node):
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return str(
            {
                "Set": self.elements
             }
        )
