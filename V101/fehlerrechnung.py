from uncertainties import ufloat
import numpy as np

D = ufloat(2.456e-2, 0.066e-2)
b = ufloat(3.571, 0.658)

print(repr((D/(2*np.pi)**2)*b-(2*3.37e-5)))
