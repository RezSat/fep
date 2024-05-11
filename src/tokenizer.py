import re
from tokens import *

class Token:
    def __init__(self, value: str, name: str, _type: str):
        self.value = value
        self.name = name
        self._type = _type

    def __repr__(self):
        return {
            "Value": self.value,
            "Name": self.name,
            "Type": self._type
        }

class Tokenier:
    def __init__(self, source: str):
        self.source = source
    
    def tokenize(self) -> list:
        c = ""
        tokens = []
        pass
