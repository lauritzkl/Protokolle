import matplotlib as mpl
mpl.use('pgf')
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})


x, y = np.genfromtxt('data3.txt', unpack=True)

def f(x, a, b):
    return (a*b)/((b + x**2)**(3/2)) 

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, r'kx', label=r'Messwerte')
plt.plot(x, f(x, *params), 'r-', label='Regression')
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\milli\tesla}$')
plt.xlabel(r'$x \, / \, \si{\meter}$')
plt.tight_layout()
plt.savefig('plot3.pdf')
