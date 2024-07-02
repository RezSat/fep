from .node import Node

class DataStructureCall(Node):
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return str(
            {
                "DataStructureCall": self.name,
                "Arguments": self.arguments
            }
        )