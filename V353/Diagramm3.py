import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

y, x = np.genfromtxt('Tabelle3.txt', unpack=True)

def f(x, a):
    return np.arctan(a*x)

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, 'kx',)
plt.plot(x, f(x, *params), 'r-', label='Regression')
plt.xlabel('$\omega/Hz$')
plt.ylabel('$\phi / rad$')
#plt.xlim(0, 10e)
plt.ylim(0, 1.75)
plt.xscale('log')
#plt.yscale('corner')
plt.tight_layout(pad=0)
plt.legend()
plt.grid()
#plt.show()
plt.savefig('Diagramm3.pdf')
print('a=', params[0],'+-', errors[0])
#print('b=', params[1],'+-', errors[1])
