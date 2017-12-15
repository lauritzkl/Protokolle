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


x, y = np.genfromtxt('data6.txt', unpack=True)
x_2, y_2 = np.genfromtxt('data6.1.txt', unpack=True)


plt.plot(x, y, r'rx', label=r'Neukurve')
plt.plot(x_2, y_2, r'kx', label=r'Hysteresekurve')
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\milli\tesla}$')
plt.xlabel(r'$I \, / \, \si{\ampere}$')
plt.tight_layout()
plt.savefig('plot6.pdf')
