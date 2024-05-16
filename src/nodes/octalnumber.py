from .node import Node

class OctalNumber(Node):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str({
            "OctalNumber": {self.value}
        })
