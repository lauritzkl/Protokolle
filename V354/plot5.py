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
plt.axvline(36500, color='green', linestyle=':', label='Resonanzfrequenz')
plt.axvline(31500, color='blue', linestyle=':', label='$\omega_1 / \omega_2$')
plt.axvline(42000, color='blue', linestyle=':')
plt.yticks([0, np.pi / 4, np.pi /2, 3 * np.pi / 4, np.pi],
[r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$"])
plt.xlabel('$\omega / \si{\Hz}$')
plt.ylabel('$\phi / rad$')
plt.tight_layout()
plt.grid()
plt.legend()
plt.savefig('plot5.pdf')
