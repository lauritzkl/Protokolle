import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x, y = np.genfromtxt('Tabelle4.txt', unpack=True)
theta = np.arctan(y*(2.865))

plt.polar(theta, x)
plt.plot(theta, x, 'kx',)
plt.legend()



plt.show()
