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


plt.plot(x, y, r'kx', label=r'Messwerte')
plt.axhline(1.478, color='green', linestyle='-', label='Theoriewert')
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\milli\tesla}$')
plt.xlabel(r'$x \, / \, \si{\meter}$')
plt.tight_layout()
plt.savefig('plot2.pdf')
