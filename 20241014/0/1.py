from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(f'{multiplier("1.1", "2.2", float)=}')
print(f'{multiplier("1.1", "2.2", Decimal)=}')
print(f'{multiplier("1/6", "2/3", Fraction)=}')
