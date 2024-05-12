#don't mind this, this is just to test inside my own computer, later will remove this
import sys
sys.path.append('/home/rezsat/Documents/github/fep/src')

from tokenizer import Tokenizer
from parser import Parser

expr = input(">> ")
tokens = Tokenizer(expr).tokenize()
parser = Parser(tokens)
ast = parser.parse()
print(ast)
