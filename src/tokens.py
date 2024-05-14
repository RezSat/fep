# Regular Expressions to match the tokens
# some RE in here are from https://github.com/python/cpython/blob/main/Lib/tokenize.py

Number = r'(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?'
Symbol = r'[a-zA-Z]' # TODO: add support for greek characters and all 
OneOperator = r'[+\-*/^=/(\);,><!|]' # supported operators if any added, edit the below list as welll
OneOperators = {
    "+": "Add",
    "-": "Subtract",
    "*": "Multiply",
    "/": "Divide",
    "^": "Power",
    "=": "Equals",
    "(": "LParen",
    ")": "RParen",
    ";": "SemiColon",
    ",": "Comma",
    '>': 'GreaterThan',
    '<': 'LessThan',
    "!": 'Factorial',
    "|": 'LBar',
}

TwoOperator = {
    ">": r'>=',
    "<": r"<=",
    "!": r"!=",
    "=": r"=="
}

TwoOperators = {
    ">=": "GTEQ",
    "<=": "LTEQ",
    "!=": "NOTEQ",
    "==": "EQEQ"
}
Word = r'\w{2,}'
Function = r'[a-zA-Z]+\(' # TODO: add support for greek characters and all 
ComplexNumber = r'([0-9](?:_?[0-9])*[iI]|(([0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?|\.[0-9](?:_?[0-9])*)([eE][-+]?[0-9](?:_?[0-9])*)?|[0-9](?:_?[0-9])*[eE][-+]?[0-9](?:_?[0-9])*)[iI])'
Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
Binnumber = r'0[bB](?:_?[01])+'
Octnumber = r'0[oO](?:_?[0-7])+'

# Keywords that the libary supports
Keywords = {
    "let": "parse_variable_assignment",
}
