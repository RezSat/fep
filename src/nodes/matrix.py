from .node import Node

class Matrix(Node):
    def __init__(self,elements=None, rows=None, cols=None, i=0):
        self.elements = elements
        self.rows = rows
        self.cols = cols
        self.data = None
        if cols != None and rows != None: 
            self.data = [[i for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        return self.data[index]

    def __str_not_use_until_needed__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def set(self, row, col, value):
        self.data[row][col] = value

    def get(self, row, col):
        return self.data[row][col]

    def shape(self):
        return (self.rows, self.cols)

    def __repr__(self):
        x = str({
            "Matrix": {
                "Rows": self.rows,
                "Columns": self.cols
            }

        })
        if self.rows != None and self.cols != None:
            return x
        else:
            return str({
                "Matrix": str(self.elements)
            })
