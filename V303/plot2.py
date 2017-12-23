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

x, y = np.genfromtxt('data2.txt', unpack=True)

def f(x, a, b):
    x = a*np.cos(y+b)
    return x

params, covariance_matrix = curve_fit(f, x, y)
errors = np.sqrt(np.diag(covariance_matrix))
#b ist die offzielle Phasenverschiebung aber ich habe eine Value error
plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x, f(y, *params), 'r-', label='Regression')
#plt.plot(y, y_t, label='Theoriekurve')
plt.legend()
plt.grid()
#plt.ylabel(r'$I \, / \, \si{\volt}$')
#plt.xlabel(r'$x \, / \, \si{\centi\meter}$')
plt.tight_layout()
plt.savefig('plot2.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
