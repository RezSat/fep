from node import Node

class Number(Node):
    def __init__(self, value: str):
        self.value = value

    @property
    def is_float(self):
        if '.' in self.value:
            return True
        return False

    @property 
    def to_dict(self):
        return {
            "Number": self.value
        }

    @property 
    def to_latex(self):
        return '\\mathtt{' + self.value + '}'

    def __float__(self):
        return float(self._as_decimal())
