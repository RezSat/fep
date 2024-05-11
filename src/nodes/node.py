class Node:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value

    def __repr__(self):
        return {"Node": self.value}

    def __str__(self):
        return str(self.__repr__)
