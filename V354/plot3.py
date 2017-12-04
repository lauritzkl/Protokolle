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
plt.axhline(1.784, color='green', linestyle=':')
plt.axvline(26000, color='blue', linestyle=':', label='Breite')
plt.axvline(42000, color='blue', linestyle=':')
plt.xlabel('$\omega / \si{Hz}$')
plt.ylabel('$U/U_0$')
plt.tight_layout()
plt.grid()
plt.legend()
#plt.yscale('log')
plt.savefig('plot3.pdf')
