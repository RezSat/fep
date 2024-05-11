import sys
sys.path.append('/home/rezsat/Documents/github/fep/src/nodes')
from number import Number

one = Number('1')
dot_one = Number('.1')
zero_dot_one = Number('0.1')

print(one.is_float)
print(one.to_dict())
print(one.to_latex())
print(one.__float__())

print(dot_one.is_float)
print(dot_one.__float__())
print(zero_dot_one.is_float)
print(zero_dot_one.__float__())

print(type(2e4))
