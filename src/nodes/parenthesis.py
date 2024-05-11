from .node import Node

class Parenthesis(Node):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f"( self.expr )"
