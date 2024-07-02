from .node import Node

class Number(Node):
    def __init__(self, value: str):
        self.value = value

    @property
    def is_float(self):
        if '.' in self.value:
            return True
        return False

    @property 
    def is_notation_exponential(self):
        if 'e' in self.value:
            return True
        return False

    def to_dict(self):
        return {
            "Number": self.value
        }

    def to_latex(self):
        return '\\mathtt{' + self.value + '}'

    def __float__(self):
        return float(self.value)

    def __repr__(self):
        return str({"Number": self.value})