a = 0.1
b = 0.2
c = a + b

print(c == 0.3)
print(c)

from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c == Decimal('0.3'))

import math
a = 0.1 + 0.2
b = 0.3
print(math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9))
