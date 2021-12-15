# Analytical Integration
import sympy as sp

# Numerical Integration
from scipy.integrate import quad
import numpy as np

# Analytical Integration

x = sp.Symbol('x')
i = sp.integrate(3.0*x**2 + 1, x)
print(i)

# Numerical Integration


def f(n):
    return 3.0 * n ** 2 + 1


# print(f(2))
i = quad(f, 0, 2)
print(i)
# print(err)

###################
# A
i2 = sp.integrate(sp.exp(-x) * sp.sin(3*x))
print(i2)

# N


def f2(y):
    return np.exp(-y) * np.sin(3.0 * y)


i3 = quad(f2, 0, 2*np.pi)
print(i3)
