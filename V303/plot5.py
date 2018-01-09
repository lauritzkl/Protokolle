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

y, x = np.genfromtxt('data4.txt', unpack=True)

def f(x, a, b):
    y = a * np.cos(x - b)
    return y

x_plot = np.linspace(0, 5, 1000)
params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))
plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Ausgleichskurve')
plt.xticks([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, 5 * np.pi / 4, 3 * np.pi / 2, 7 * np.pi / 4, 2 * np.pi],
           [r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$", r"$\frac{5}{4}\pi$", r"$\frac{3}{2}\pi$", r"$\frac{7}{4}\pi$", r"$2\pi$"])
plt.legend()
plt.grid()
plt.ylabel(r'$U_{out} \, / \, \si{\volt}$')
plt.xlabel(r'$\phi \, / \, rad$')
plt.tight_layout()
plt.savefig('plot5.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
