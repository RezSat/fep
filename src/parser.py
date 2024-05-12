from nodes import *
from tokens import Keywords
"""
TODO:
parenthesis means multiplication ( well sometimes )
statement separation
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
        # fix errors like let x = 4x = 6 -> {'Equation': {'Left': {'Variable': 'x', 'Value': {'BinaryOperation': '*', 'Left': {'Number': '4'}, 'Right': {'Symbol': 'x'}}}, 'Right': None}}
        if self.current_token != None and self.current_token.value == "=":
            right = self.parse_expression()
            return Equation(node, right)
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

        if self.current_token.value == "(":
            self.advance()
            node = self.parse_expression()
            if self.current_token != None and self.current_token.value != ")":
                self.advance()
                node = Parenthesis(node)
            else:
                SyntaxError("Parenthesis Missing or Mismatch Error: expected `)`")

        elif self.current_token.name == "Number":
            node = Number(self.current_token.value)
            self.advance()
            if self.current_token != None and self.current_token.name == "Symbol":
                node = Multiply(left=node, right=Symbol(self.current_token.value))
                self.advance()

        elif self.current_token.name in ("Symbol", "Word"):
            if self.current_token.value in Keywords:
                parse_method = getattr(self,Keywords[self.current_token.value])
                node = parse_method()
            else:
                node = Symbol(self.current_token.value)
                self.advance()

        elif self.current_token.name == "Function":
            node = self.parse_function_define()
        
        return self.parse_power(node)
    
    def parse_power(self, node):
        if self.current_token != None and self.current_token.value == "^":
            op = self.current_token.value
            operator_ = globals()[self.current_token.name]
            self.advance()
            node = operator_(base=node, index=self.parse_factor())
        
        return self.parse_function_call(node)
    
    def parse_function_call(self, node):
        if self.current_token != None and self.current_token.name == 'Function':
            func_name = self.current_token.value
            self.advance()
            if self.current_token.value == "(":
                self.advance()
                arguments = []
                if self.current_token.name in ('Symbol', 'Word', "Number"):
                    arguments.append(self.parse_factor())
                
                while self.current_token.value == ',':
                    self.advance()
                    arguments.append(self.parse_factor())

                if self.current_token != None and self.current_token.value == ')':
                    self.advance()
                    return FunctionCall(func_name, arguments)
                else:
                    SyntaxError("Parenthesis Mismatch or Missing: expected `)`")
        return node

    def parse_function_define(self):
        if self.current_token.name == "Function":
            func_name = self.current_token.value
            self.advance()
            if self.current_token.value == "(":
                self.advance()
                arguments = []
                if self.current_token.name in ("Symbol", "Word"):
                    arguments.append(self.current_token)
                    self.advance()

                while self.current_token.value == ',':
                    self.advance()
                    arguments.append(self.current_token)
                    self.advance()

                if self.current_token != None and self.current_token.value == ')':
                    self.advance()
                else:
                    SyntaxError("Parenthesis Mismatch or Missing: expected `)`")
                
                if self.current_token != None and self.current_token.value == '=':
                    self.advance()
                    body = self.parse_expression()

                    node = FunctionDefinition(func_name, arguments, body)
                    return node
                else:
                    node = FunctionCall(func_name, arguments)
                    return node
    
    def parse_variable_assignment(self):
        # this also can do this `let x = f(x) = 4x+5`
        # whether I like or not I haven't decide that yet.
        if self.current_token.value == 'let':
            self.advance()
            if self.current_token != None and self.current_token.name in ('Symbol', 'Word'):
                var_name = self.current_token.value
                self.advance()
            else:
                SyntaxError("No Variable Name or Invalid Variable Name Found")

            if self.current_token != None and self.current_token.value == '=':
                self.advance()
            else:
                SyntaxError('Syntax Error: `=` expected ')

            expr = self.parse_expression()

            return VariableAssignment(var_name, expr)
