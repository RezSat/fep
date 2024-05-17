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

class MatrixAssignment(Node):
    def __init__(self, name, value, n=0, m=None):
        self.m = m
        self.n = n
        self.name = name
        self.value = value

    def __repr__(self):
        return str({
            "MatrixAssignment": {
                "MatrixName": self.name,
                "Value": self.value,
                "Row": self.n,
                "Column": self.m
            }
        })