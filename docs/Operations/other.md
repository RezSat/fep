# Other Operations

### Percentage

Path: `fep/src/nodes/percentage.py`

Params: value

Symbol: `%`

Examples: `20%`

``` py
class Percentage(Node):
    def __init__(self, value):
        self.value = value

```

### Modulus

Path: `fep/src/nodes/modulus.py`

Params: expr

Symbol: `|` expr `|`

Examples: `|-2|`

``` py
class Modulus(Node):
    def __init__(self, expr):
        self.expr = expr
```

### Factorial

Path: `fep/src/nodes/factorial.py`

Params: value

Symbol: `!`

Examples: `5!`

``` py
class Factorial(Node):
    def __init__(self, value):
        self.value = value
```

### Parenthesis

Path: `fep/src/nodes/parenthesis.py`

Params: expr

Symbol: `(` expr `)`

Examples: `(3+2-6x)`

``` py
class Parenthesis(Node):
    def __init__(self, expr):
        self.expr = expr

```