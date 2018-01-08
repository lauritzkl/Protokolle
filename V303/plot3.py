from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
# from uncertainties import ufloat
U, p = np.genfromtxt('data2.txt', unpack=True)
phi = np.linspace(0, 5, 1000)
t = np.linspace(0, 5, 1000)
#-0.3, 8, 1000
def f(x, a, b):
    return b * np.cos(x - a)

params, cov = curve_fit(f, p, U)
errP = np.sqrt(np.diag(cov))
print('a =', params[0], '+/-', errP[0])
print('b =', params[1], '+/-', errP[1])
#print('c =', params[2], '+/-', errP[2])
plt.plot(p, U, 'kx', label='Messwerte')
plt.plot(phi, f(phi, *params), 'r-', label='Ausgleichskurve')
#plt.plot(t, f(t, 0, params[1], 0), 'g-', label='Theoriekurve')
plt.xlabel(r'$\phi\:/\:rad$')
plt.ylabel(r'$U\:/\:V$')
plt.legend(loc='best')
plt.xticks([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, 5 * np.pi / 4, 3 * np.pi / 2, 7 * np.pi / 4, 2 * np.pi],
           [r"$0$", r"$\frac{1}{4}\pi$", r"$\frac{1}{2}\pi$", r"$\frac{3}{4}\pi$", r"$\pi$", r"$\frac{5}{4}\pi$", r"$\frac{3}{2}\pi$", r"$\frac{7}{4}\pi$", r"$2\pi$"])
plt.xlim(-0.2, 0.2 + 2 * np.pi)
plt.grid()
plt.tight_layout()
plt.savefig('kurve1.pdf')
