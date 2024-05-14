from .node import Node

class Vector(Node):
    def __init_(self, row=None):
        #just a one-dimensional matrix maybe no need to use but incase needed
        self.row = row

    def __repr__(self):
        return str(
            {
                "Vector": self.row
            }
        )


