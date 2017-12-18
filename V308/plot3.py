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


x, y = np.genfromtxt('data3.txt', unpack=True)
x_2 = np.linspace(0.008, 0.17)

y_2=(1.26*10**(-6)*3)/(0.14)*((1/(((x_2-0.035)/0.07)**2+((x_2-0.035)/0.07)+(5/4))**(3/2))+(1/(((x_2-0.035)/0.07)**2-((x_2-0.035)/0.07)+(5/4))**(3/2)))

plt.plot(x, y, r'kx', label=r'Messwerte')
plt.plot(x_2, y_2)
plt.legend()
plt.grid()
plt.ylabel(r'$B \, / \, \si{\tesla}$')
plt.xlabel(r'$x \, / \, \si{\meter}$')
plt.tight_layout()
plt.savefig('plot3.pdf')
