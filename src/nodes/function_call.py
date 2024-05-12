from .node import Node

class FunctionCall(Node):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return str(
            {
                "FunctionCall": self.name,
                "Arguments": self.arguments
            }
        )
