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

y, x= np.genfromtxt('Data3.txt', unpack=True)


plt.plot(x, y, r'kx', label=r'Messwerte')
plt.legend()
plt.yticks([0, np.pi / 4, np.pi /2, 3 * np.pi / 4, np.pi],
[r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.xlabel('$\omega / \si{\Hz}$')
plt.ylabel('$\phi / rad$')
plt.xscale('log')
plt.tight_layout()
plt.savefig('plot4.pdf')
