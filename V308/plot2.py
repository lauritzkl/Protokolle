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

x_3 = np.linspace(0.01, 0.12, 23)

y_3 = (4*np.pi*10**(-7)*1176.47*1.3)/2 * ((x-0.03)/((x-0.03)**2 + 0.0205**2)**(1/2) - (x-0.095)/((x-0.095)**2 + 0.0205**2)**(1/2))

plt.plot(x, y, r'kx', label=r'Messwerte')
plt.plot(x_3, y_3, label='Theoriekurve')
#plt.axhline(1.478, color='green', linestyle='-', label='Theoriewert')
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\tesla}$')
plt.xlabel(r'$x \, / \, \si{\meter}$')
plt.tight_layout()
plt.savefig('plot2.pdf')
