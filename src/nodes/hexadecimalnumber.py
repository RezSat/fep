from .node import Node

class HexaDecimalNumber(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str({
            "HexaDecimalNumber": {self.value}
        })
