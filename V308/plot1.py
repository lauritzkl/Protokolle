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


x, y = np.genfromtxt('data1.txt', unpack=True)
x_2, y_2 = np.genfromtxt('data1.2.txt', unpack=True)


plt.plot(x, y, r'kx', label=r'Messwerte links')
plt.plot(x_2, y_2, r'rx', label=r'Messwerte rechts')
plt.axhline(1.984, color='green', linestyle='-', label='Theoriewert')
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\milli\tesla}$')
plt.xlabel(r'$x \, / \, \si{\meter}$')
plt.tight_layout()
plt.savefig('plot1.pdf')
