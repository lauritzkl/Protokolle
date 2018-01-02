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

x_1 = np.linspace(14.5, 132.5, 26)

y_1 = 6.65 * ((14.5**2)/(x**2))


plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x_1, y_1, label='Theoriekurve')
#plt.plot(y, y_t, label='Theoriekurve')
plt.legend()
plt.grid()
plt.ylabel(r'$I \, / \, \si{\volt}$')
plt.xlabel(r'$x \, / \, \si{\centi\meter}$')
plt.tight_layout()
plt.savefig('plot4.pdf')
