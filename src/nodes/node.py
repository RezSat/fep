class Node:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        method_name = f'visitor_{self.__class__.__name__}'
        visitor_method = getattr(visitor, method_name, None)
        if visitor_method:
            visitor_method(self)
        else:
            raise NotImplementedError(f"{method_name} is not Implemented.")
    

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value

    def __repr__(self):
        return {"Node": self.value}

    def __str__(self):
        return str(self.__repr__)
    
    def __hash__(self):
        return hash(self.value)
