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

y, x = np.genfromtxt('data2.txt', unpack=True)

def f(x, a, b):
    y = a*x + b
    return y

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x, f(x, *params), 'r-', label='Ausgleichskurve')
plt.legend()
plt.grid()
plt.ylabel(r'$U_{k} \, / \, \si{\volt}$')
plt.xlabel(r'$I \, / \, \si{\ampere}$')
plt.tight_layout()
plt.savefig('plot2.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
