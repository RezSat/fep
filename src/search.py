from .visitor import Visitor

class PreOrder(Visitor):
    def __init__(self):
        pass

    def visit(self, node):
        node.visit(self)


class PostOrder(Visitor):
    def __init__(self):
        pass

    def visit(self, node):
        node.visit(self)
