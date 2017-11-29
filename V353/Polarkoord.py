import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y = np.genfromtxt('Tabelle4.txt', unpack=True)

x_plot= np.linspace(0, 50, 100)

plt.polar(x, y)
#plt.plot(x_plot)
plt.legend()


plt.savefig('Polar.pdf')
