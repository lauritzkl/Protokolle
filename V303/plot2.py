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
    y = a*np.cos(x + b)
    return y

x_plot = np.linspace(0, 5, 1000)
t = np.linspace(0, 5, 1000)
params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))
#b ist die offzielle Phasenverschiebung aber ich habe eine Value error
plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression')
plt.plot(t, f(t, *params), 'b-', label='Theoriekurve')
plt.xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2],
            [r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$",  r"$\frac{3\pi}{4}$", r"$\pi$",
             r"$\frac{5\pi}{4}$", r"$\frac{3\pi}{2}$"])
plt.legend()
plt.grid()
plt.ylabel(r'$U_{out} \, / \, \si{\volt}$')
plt.xlabel(r'$\phi \, / \, rad$')
plt.tight_layout()
plt.savefig('plot2.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
