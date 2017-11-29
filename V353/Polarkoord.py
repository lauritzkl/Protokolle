import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y = np.genfromtxt('Tabelle4_1.txt', unpack=True)

def f(x, a, b):
    y = -(x/a) + b
    return y

params, covariance_matrix = curve_fit(f, x, y)

x_plot = np.linspace(0, 1.6, 1000)

plt.polar(x, y, 'kx', label='Messwerte')
plt.polar(x_plot, f(x_plot, *params), 'r-', label='Regression')
#plt.plot(x_plot)
plt.legend()


plt.savefig('Polar.pdf')
