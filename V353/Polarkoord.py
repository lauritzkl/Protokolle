import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

r = np.genfromtxt('Tabelle3.txt', unpack=True)
theta = r

plt.polar(theta)
plt.show()
