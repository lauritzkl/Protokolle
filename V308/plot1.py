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
#x_3, D = np.genfromtxt('data1.3.txt', unpack=True)
x_3 = np.linspace(0.01, 0.21)
y_3 = (4*np.pi*10**(-7)*1578.95*1.1)/2 * ((x_3-0.02)/((x_3-0.02)**2 + 0.0205**2)**(1/2) - (x_3-0.2)/((x_3-0.2)**2 + 0.0205**2)**(1/2))


plt.plot(x, y, r'kx', label=r'Messwerte links')
plt.plot(x_2, y_2, r'rx', label=r'Messwerte rechts')
plt.plot(x_3, y_3, label='Theoriekurve')
#plt.axhline(0.001984, color='green', linestyle='-', label='Theoriewert')
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\tesla}$')
plt.xlabel(r'$x \, / \, \si{\meter}$')
plt.tight_layout()
plt.savefig('plot1.pdf')
