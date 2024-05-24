from .node import Node

class LogicalOperator(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return str(
            {
                "LogicalOperator": self.op,
                "Left": self.left,
                "Right": self.right
            }
        )

class LogicalOr(LogicalOperator):
    def __init__(self, left, right):
        super().__init__(left=left, op="or", right=right)

class LogicalAnd(LogicalOperator):
    def __init__(self, left, right):
        super().__init__(left=left, op="and", right=right)

class LogicalNot(LogicalOperator):
    def __init__(self, right):
        super().__init__(left=None, op="not", right=right)

class LogicalXor(LogicalOperator):
    def __init__(self, left, op, right):
        super().__init__(left=left, op="xor", right=right)