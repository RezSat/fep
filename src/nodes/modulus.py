from .node import Node

class Modulus(Node):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return str({
            "ModulusOperator": f"| {self.expr} |"
        })
