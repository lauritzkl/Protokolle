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


y, x = np.genfromtxt('data.txt', unpack=True)
#y_t = 1/x**2
# Ich weiß nicht wie man die Theorie kurve da reinbekommt help me pls!!! :D

plt.plot(x, y, r'kx', label='Messwerte')
#plt.plot(y, y_t, label='Theoriekurve')
plt.legend()
plt.grid()
plt.ylabel(r'$I \, / \, \si{\volt}$')
plt.xlabel(r'$r \, / \, \si{\centi\meter}$')
plt.tight_layout()
plt.savefig('plot1.pdf')
