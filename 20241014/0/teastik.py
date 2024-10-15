from math import *
from decimal import Decimal
import decimal
from fractions import Fraction

print(Fraction(11, 10) * 8 / 23)
decimal.getcontext().prec = 100

print(Decimal("1.1") + Decimal("2.2"))
print(Decimal(1.1) + Decimal(2.2))

print(Decimal("1.44").sqrt())
