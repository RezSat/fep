from .node import Node

class FunctionDefinition(Node):
    def __init__(self, name, arguments, body):
        self.name = name
        self.arguments = arguments
        self.body = body

    def __repr__(self):
        return str({
            "FunctionDefinition": self.name,
            "Arguments": self.arguments,
            "Body": self.body
        })
