import matplotlib.pyplot as plt
import numpy as np


def f(x, a, b, c):
    """

    :Ovo je kvadratna funkcija i prima 4 parametara:

    :param x: ovaj parametar nema ogranicenja
    :param a: ovaj parametar mora da bude pozitivan
    :param b: ovaj parametar mora da bude pozitivan
    :param c: ovaj parametar ne sme da bude nula (0)
    :return: a*x**2 + b*x + c
    """
    return a*x**2 + b*x + c


lista = np.linspace(-10, 10, num=100)
listb = f(lista, 3, 1, 4)


plt.figure(num=0, dpi=100)
plt.plot(lista, listb, label='f(a*x**2 + b*x + c)')
plt.plot(lista, lista**2, label='f(x**2)')
plt.legend()
plt.show()
