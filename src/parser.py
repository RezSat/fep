from nodes import *

"""
TODO:
basic arithmetic
parenthesis
one-line function definition
function calls
coefficiet-symbol
parenthesis means multiplication ( well sometimes )
statement separation
variable assignments
equation
inequality

data-strctures:
    matrices
    hash-maps/dicts
    sets


more later
"""
class Parser:
    def __init__(self, tokens: list):
        self.tokens = iter(tokens)
        self.current_token = next(self.tokens)

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        node = self.parse_expression() 
        return node

    def parse_expression(self):
        node = self.parse_term()

        while self.current_token != None and self.current_token.value in ("+", "-"):
            operator_ = globals()[self.current_token.name]
            self.advance()
            right = self.parse_term()
            node = operator_(left=node, right=right) # Add(left, right) or Subtract(left, right)
        return node

    def parse_term(self):
        node = self.parse_factor()

        while self.current_token != None and self.current_token.value in ("*", "/"):
            operator_ = globals()[self.current_token.name]
            self.advance()
            right = self.parse_factor()
            node = operator_(left=node, right=node)
        
        return node

    def parse_factor(self):
        node = None

        if self.current_token.name == "Number":
            node = Number(self.current_token.value)
            self.advance()
        return node

