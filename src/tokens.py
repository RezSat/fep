# Regular Expressions to match the tokens
# some RE in here are from https://github.com/python/cpython/blob/main/Lib/tokenize.py
# https://unicode-table.com/en/
# https://www.wikiwand.com/en/Mathematical_operators_and_symbols_in_Unicode

Number = r'(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?'
Symbol = r'[a-zA-Z_α-ωΑ-Ω\u2100-\u214F\u2200-\u22FF\u2190-\u21FF\u27C0-\u27EF\u2980-\u29FF\u2A00-\u2AFF\u2B00-\u2BFF]'
OneOperator = r'[+\-*/^=/(\);,><!|[\]%]' # supported operators if any added, edit the below list as welll
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
    '[': 'LBracket',
    ']': 'RBracket',
    '%': 'Percentage',
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
Word = r'[a-zA-Zα-ωΑ-Ω\u2100-\u214F\u2200-\u22FF\u2190-\u21FF\u27C0-\u27EF\u2980-\u29FF\u2A00-\u2AFF\u2B00-\u2BFF\w]{2,}'
#latin, greek, or letter-like character
Function = r'[a-zA-Zα-ωΑ-Ω\u2100-\u214F\u2200-\u22FF\u2190-\u21FF\u27C0-\u27EF\u2980-\u29FF\u2A00-\u2AFF\u2B00-\u2BFF_]+\('
ComplexNumber = r'(\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?[+-](\d+(\.\d+)?|\.\d+)([eE][+-]?\d+)?[iI]'
#ComplexNumber = r'([0-9](?:_?[0-9])*[iI]|(([0-9](?:_?[0-9])*\.(?:[0-9](?:_?[0-9])*)?|\.[0-9](?:_?[0-9])*)([eE][-+]?[0-9](?:_?[0-9])*)?|[0-9](?:_?[0-9])*[eE][-+]?[0-9](?:_?[0-9])*)[iI])'
Hexnumber = r'0[xX](?:_?[0-9a-fA-F])+'
Binnumber = r'0[bB](?:_?[01])+'
Octnumber = r'0[oO](?:_?[0-7])+'

# Keywords that the libary supports
Keywords = {
    'let': "parse_variable_assignment",
    'and': "parse_logical_and",
    'or': "parse_logical_or",
    'xor': "parse_logical_xor",
    #not is handled in parse_factor separately
    'bitwiseOr': "",
    'bitwiseXor': "",
    'bitwiseAnd': "",
}