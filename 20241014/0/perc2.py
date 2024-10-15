from fractions import Fraction as frac
import decimal

decimal.getcontext().prec = 10

from fractions import Fraction

def esum(N, one):
    res = one
    fact = one
    for i in range(1, N):
        fact *= i
        res += one / fact
    return res

print(f'{esum(100, decimal.Decimal(1))}')
