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

y, x = np.genfromtxt('data5.txt', unpack=True)

x_plot = np.linspace(3.75, 65, 10000)

y_plot = x_plot*1.63**2/(x_plot + 16.82)**2


plt.plot(x, y, r'kx', label='Messwerte')
plt.plot(x_plot, y_plot, 'r-', label='Theoriekurve')
plt.legend()
plt.grid()
plt.ylabel(r'$N \, / \, \si{\watt}$')
plt.xlabel(r'$R_a \, / \, \si{\ohm}$')
plt.tight_layout()
plt.savefig('plot5.pdf')
print(x*1.63**2/(x + 16.82)**2)
