import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y, x = np.genfromtxt('Tabelle.txt', unpack=True)

def f(x, a, b):
    return (-1/a) * x + b

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, 'kx',)
plt.plot(x, f(x, *params), 'r-', label='Regression')
plt.xlabel('t / ms')
plt.ylabel('ln({Uc}/{U0})')
#plt.xlim(1.5e-2, 9e-2)
#plt.ylim(1.5e-3, 5e-3)
plt.tight_layout(pad=0)
plt.legend()
plt.grid()
#plt.show()
plt.savefig('Diagramm1.pdf')
print('a=', params[0],'+-', errors[0])
print('b=', params[1],'+-', errors[1])
