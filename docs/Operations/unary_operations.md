# Unary Operations

path : `fep/src/nodes/unary_op.py`

### Positive

Params:  right

Symbol: `+`

``` py
class Positive(UnaryOperation):
    def __init__(self, value):
        super().__init__(op="+", value=value)
```


### Negative

Params:  right

Symbol: `-`

``` py

class Negative(UnaryOperation):
    def __init__(self, value):
        super().__init__(op="-", value=value)
```