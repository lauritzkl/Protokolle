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

y, x= np.genfromtxt('Data2.txt', unpack=True)


plt.plot(x, y, r'kx', label=r'Messwerte')
plt.xscale('log')
plt.xlabel('$\omega / \si{Hz}$')
plt.ylabel('$U/U_0$')
plt.tight_layout()
plt.legend()
#plt.yscale('log')
plt.savefig('plot2.pdf')
