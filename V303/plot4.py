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

y, x = np.genfromtxt('data3.txt', unpack=True)

def f(x, a):
    y = a/x**2
    return y

x_plot = np.linspace(14, 133, 1000)

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression')
plt.legend()
plt.grid()
plt.ylabel(r'$I \, / \, \si{\volt}$')
plt.xlabel(r'$r \, / \, \si{\centi\meter}$')
plt.tight_layout()
plt.savefig('plot4.pdf')
print('a=', params[0], '+-', errors[0])
