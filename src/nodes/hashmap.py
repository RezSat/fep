from .node import Node

class HashMap(Node):
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values
        self.pairs = dict(zip(keys, values))

    def __repr__(self):
        return str(
            {
                "HashMap": self.pairs
             }
        )