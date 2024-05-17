#don't mind this, this is just to test inside my own computer, later will remove this
import sys
sys.path.append('/home/rezsat/Documents/github/fep/src')

from tokenizer import Tokenizer
from parsing import Parser

expr = input(".>> ")
#expr = """
#[[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
#"""
tokens = Tokenizer(expr).tokenize()
print(tokens)

print('\n\n')
parser = Parser(tokens)
ast = parser.parse()
print(ast)
