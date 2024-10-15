from decimal import Decimal
from fractions import Fraction

def esum(N, one):
    res = one
    fact = one
    for i in range(1, N):
        fact *= i
        res += one / fact
    return res

print(f'{esum(100, Decimal(1))}')
print(f'{esum(100, Fraction(1))}')
print(f'{esum(100, 1.0)}')
print(f'{esum(10, 1)}')


import decimal
decimal.getcontext().prec = 100
olde = 0
for i in range(20, 100): 
    new = esum(i, decimal.Decimal(1))
    if new == olde:
        break
    olde == new
print(new, i)
