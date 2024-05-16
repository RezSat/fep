from nodes import *
from tokens import Keywords
"""
TODO:
we don't allow this -> parenthesis means multiplication (because of how the functions are there but if we fix the tokenization process this might can be allowed)
if-conditions ( or similar)
loops (similar/exact to while and for)
handle implicit multiplication and division properly

mixed numbers
fractions 
squareroots/nth root
polynomial terms - coefficents like this: (3+2x)x^2
bitwise operators
handle underscores on variables, function names so that subscript can be done from front_end.

parse : 'A[1,2] = 4'
factorial
x′ - complement operators ( not sure if need right now )
maybe take all assignments to one place like variable assignments, matrix assignments and function assignments
data-strctures:
    hash-maps/dicts
    sets

# not sure if needed, but we can use arrows (`->`) for mapping, variable assigning or somthing similar to that

handle different other unicode characters

more later
"""
class Parser:
    def __init__(self, tokens: list):
        self.tokens = iter(tokens)
        self.current_token = next(self.tokens)
        self.lbar_open = 0
        self.lbar_close = 0

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        statements = []
        while self.current_token is not None:
            node = self.parse_expression()
            # fix or handle errors like let x = 4x = 6 -> {'Equation': {'Left': {'Variable': 'x', 'Value': {'BinaryOperation': '*', 'Left': {'Number': '4'}, 'Right': {'Symbol': 'x'}}}, 'Right': None}}
            if self.current_token != None and self.current_token.value == "=":
                self.advance()
                right = self.parse_expression()
                statements.append(Equation(node, right))
            elif self.current_token != None and self.current_token.value in ("<", ">", "!=", ">=", "<="):
                op = self.current_token.value
                self.advance()
                right = self.parse_expression()
                statements.append(Inequality(node, op, right))
            else:
                statements.append(node)

            if self.current_token != None and self.current_token.value == ';':
                self.advance()
            else:
                break
        return statements

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
            node = operator_(left=node, right=right)
        
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

        elif self.current_token.value == '[':
            self.advance()
            elements = []
            while self.current_token != None and self.current_token.value != ']':
                element = self.parse_expression()
                elements.append(element)
                if self.current_token == None:
                    raise SyntaxError("Missing closing ']' for matrix")
                elif self.current_token.value == ',':
                    self.advance()
            if self.current_token == None or self.current_token.value != ']':
                raise SyntaxError("Missing closing ']' for matrix")

            self.advance()
            node = Matrix(elements)

        elif self.current_token.value == "|":
            self.advance()
            node = self.parse_expression()
            if self.current_token != None and self.current_token.value == "|":
                self.advance()
                node = Modulus(node)
            else:
                SyntaxError("Mismatached Modulus operator: expected : `|`")

        elif self.current_token.value == "+":
            self.advance()
            node = Positive(value=self.parse_factor())

        elif self.current_token.value == "-":
            self.advance()
            node = Negative(value=self.parse_factor())
        
        elif self.current_token.name == "ComplexNumber":
            node = ComplexNumber(self.current_token.value)

        elif self.current_token.name == "HexaDecimalNumber":
            node = HexaDecimalNumber(self.current_token.value)

        elif self.current_token.name == "OctalNumber":
            node = OctalNumber(self.current_token.value)

        elif self.current_token.name == "BinaryNumber":
            node = BinaryNumber(self.current_token.value)

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
        # Issue maybe should change the Function token name, since its there there is really no use of having a separate function-call parse functions as it is being parsed from the function-define anyways, but since functin-call shoul have higher precendence i should handle them differently, so instead of separating that in the lexing state it should be handle while parsing.
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
                if self.current_token.name in ("Symbol", "Word", "Number"):
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


