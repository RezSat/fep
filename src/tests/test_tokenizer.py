#don't mind this, this is just to test inside my own computer, later will remove this
import sys
sys.path.append('/home/rezsat/Documents/github/fep/src')

from tokenizer import Tokenizer

expr = "2+4=*9(877)+3-4i*2e5+f(x)-;let x = 4"
tokenier = Tokenizer(expr)
tokens = tokenier.tokenize()
print(tokens)


