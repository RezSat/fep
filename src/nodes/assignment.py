from .node import Node

class VariableAssignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return str(
            {
                "Variable": self.name,
                "Value": self.value
            }
        )
