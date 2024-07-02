# Binary Operations

path : `fep/src/nodes/binary_op.py`

### Addition

Params: left, right

Symbol: `+`

``` py
class Add(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left=left, op="+", right=right)
```

### Subtraction
Params: left, right

Symbol: `-`

``` py
class Subtract(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "-", right)
```

### Multiplication
Params: left, right

Symbol: `*`

``` py
class Multiply(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "*", right)
```

### Division
Params: left, right

Symbol: `/`

``` py
class Divide(BinaryOperation):
    def __init__(self, left, right):
        super().__init__(left, "/", right)

```

### Power

Params: base, index

Symbol: `^`

``` py

class Power(BinaryOperation):
    def __init__(self, base, index):
        super().__init__(base, "^", index)
```