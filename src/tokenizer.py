import re
from tokens import *

class Token:
    def __init__(self, value: str, name: str, _type: str):
        self.value = value
        self.name = name
        self._type = _type

    def __repr__(self):
        return str({
            "Value": self.value,
            "Name": self.name,
            "Type": self._type
        })
    

class Tokenizer:
    def __init__(self, source: str):
        self.source = source
    
    def tokenize(self) -> list:
        c = ""
        tokens = []
        while self.source:
            match = re.match(Function, self.source)
            if match:
                value = match.group()[:-1]
                tokens.append(Token(value,"Function", "Operand"))
                self.source = self.source[len(value):]
                continue
            
            match = re.match(ComplexNumber, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, "ComplexNumber", "Operand"))
                self.source = self.source[len(value):]
                continue

            match = re.match(Hexnumber, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, "HexaDecimalNumber", "Operand"))
                self.source = self.source[len(value):]
                continue

            match = re.match(Binnumber, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, 'BinaryNumber', "Operand"))
                self.source = self.source[len(value):]
                continue

            match = re.match(Octnumber, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, "OctalNumber", "Operand"))
                self.source = self.source[len(value):]
                continue
            
            match = re.match(Number, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, "Number", "Operand"))
                self.source = self.source[len(value):]
                continue

            match = re.match(Word, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, "Word", "Operand"))
                self.source = self.source[len(value):]
                continue

    
            match = re.match(Symbol, self.source)
            if match:
                value = match.group()
                tokens.append(Token(value, "Symbol", "Operand"))
                self.source = self.source[len(value):]
                continue

            match = re.match(OneOperator, self.source)
            if match:
                value = match.group()
                if value in TwoOperator.keys():
                    if match := re.match(TwoOperator[value], self.source):
                        value = match.group()
                        tokens.append(Token(value, TwoOperators[value], "Operator"))
                        self.source = self.source[len(value):]
                        continue
                    else:
                        tokens.append(Token(value, OneOperators[value], "Operator"))
                        self.source = self.source[len(value):]
                        continue
                else:
                    tokens.append(Token(value, OneOperators[value], "Operator"))
                    self.source = self.source[len(value):]
                    continue

            if self.source[0].isspace():
                self.source = self.source[1:]
                continue

            raise ValueError(f"Invalid character: {self.source[0]}")
        return tokens
