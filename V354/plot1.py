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


y, x, y_2, x_2 = np.genfromtxt('Data1.txt', unpack=True)

def f(x, a, b):
    y = a*np.exp(-b*x)
    return y

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

def g(x_2, c, d):
    y_2 =  -c*np.exp(-d*x)
    return y_2

params1, covariance_matrix1 = curve_fit(g, x_2, y_2)

errors1 = np.sqrt(np.diag(covariance_matrix1))

#x = np.linspace(0,305, 1000)
#x_2 = np.linspace(0,305, 1000)

plt.plot(x, y, r'kx', label=r'Messwerte Max')
plt.plot(x, f(x, *params), 'r-', label='Regression Max')
plt.plot(x_2, y_2, r'bx', label='Messwerte Min')
plt.plot(x_2, g(x_2, *params1), 'g-', label='Regression Min')
plt.legend()
plt.grid()
plt.ylabel(r'$U_c / \si{\V}$')
plt.xlabel(r'$t / \SI{e-6}{\second}$')
plt.tight_layout()
plt.savefig('plot1.pdf')
print('a=', params[0], '+-', errors[0])
print('b=', params[1], '+-', errors[1])
print('c=', params1[0], '+-', errors1[0])
print('d=', params1[1], '+-', errors1[1])
