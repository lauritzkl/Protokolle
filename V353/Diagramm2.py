import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import sem

y, x = np.genfromtxt('Tabelle2.txt', unpack=True)

def f(x, a):
    y = 1 / np.sqrt(1 + (a*x)**2)
    return y

x_plot = np.linspace(0, 10e3, 1000)

params, covariance_matrix = curve_fit(f, x, y)

errors = np.sqrt(np.diag(covariance_matrix))

plt.plot(x, y, 'kx',)
plt.plot(x_plot, f(x_plot, *params), 'r-', label='Regression')
plt.xlabel('$\omega / Hz$')
plt.ylabel('$A/U_0$')
plt.xscale('log')
#plt.xlim(0, 10e3)
#plt.ylim(0, 0.5)
#plt.tight_layout(pad=0)
plt.savefig('Diagramm2.pdf')

print('a=', params[0],'+-', errors[0])

#default_seed = (1,1,1)
#good_seed = (-1,1,1)
#parameter = [default_seed, good_seed, params]
#for p in parameter:
    #plt.plot(x, sigmoid(x, *p))
