# Logical Operations

path : `fep/src/nodes/logical_operators.py`

### Logical AND

Params: left, right

Symbol: `and`

``` py
class LogicalAnd(LogicalOperator):
    def __init__(self, left, right):
        super().__init__(left=left, op="and", right=right)
```

### Logical OR

Params: left, right

Symbol: `or`

``` py
class LogicalOr(LogicalOperator):
    def __init__(self, left, right):
        super().__init__(left=left, op="or", right=right)
```

### Logical XOR

Params: left, right

Symbol: `xor`

``` py
class LogicalXor(LogicalOperator):
    def __init__(self, left, op, right):
        super().__init__(left=left, op="xor", right=right)
```

### Logical NOT

Params:  right

Symbol: `not`

``` py
class LogicalNot(LogicalOperator):
    def __init__(self, right):
        super().__init__(left=None, op="not", right=right)
```