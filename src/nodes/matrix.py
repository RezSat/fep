from .node import Node

class Matrix(Node):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def __repr__(self):
        return str({
            "Matrix": {
                "Rows": self.rows,
                "Columns": self.cols
            }

        })
