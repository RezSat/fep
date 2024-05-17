class Visitor():
    """
    visit methods inside this class is in sync with the __all__ in the nodes/__init__.py, 
    any edits there should be made here as well so this class is up-to-date with the nodes
    properly. Also make note of the ordering, its easier if kept the order of these visit methods
    in match with the __all__ list as well.
    """
    def visit(self, node):
        return node.accept(self)

    def visit_Node(self, node):
        pass

    def visit_Number(self, node):
        pass

    def visit_Symbol(self, node):
        pass

    def visit_Add(self, node):
        pass

    def visit_Subtract(self, node):
        pass

    def visit_Multiply(self, node):
        pass

    def visit_Divide(self, node):
        pass

    def visit_Power(self, node):
        pass

    def visit_Positive(self, node):
        pass

    def visit_Negative(self, node):
        pass

    def visit_Parenthesis(self, node):
        pass

    def visit_FunctionDefinition(self, node):
        pass

    def visit_FunctionCall(self, node):
        pass

    def visit_VariableAssignment(self, node):
        pass

    def visit_MatrixAssignment(self, node):
        pass

    def visit_Equation(self, node):
        pass

    def visit_Inequality(self, node):
        pass

    def visit_Matrix(self, node):
        pass

    def visit_Vector(self, node):
        pass

    def visit_Set(self, node):
        pass

    def visit_Modulus(self, node):
        pass

    def visit_ComplexNumber(self, node):
        pass

    def visit_HexaDecimalNumber(self, node):
        pass

    def visit_OctalNumber(self, node):
        pass

    def visit_BinaryNumber(self, node):
        pass

    def visit_Percentage(self, node):
        pass

    def visit_Factorial(self, node):
        pass