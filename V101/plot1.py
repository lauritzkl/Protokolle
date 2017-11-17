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


V1, V2, y, x = np.genfromtxt('data1.txt', unpack=True)

def f(x, a, b):
    return a * x + b

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(0,750e-4)

plt.plot(x, y, r'kx', label=r'Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression')
plt.legend()
plt.grid()
plt.ylabel(r'$T^2 \, \text{in} \, \si{\second\squared}$')
plt.xlabel(r'$a^2 \, \text{in} \, \si{\meter\squared}$')
plt.tight_layout()
plt.savefig('ausgleichsgerade1.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
