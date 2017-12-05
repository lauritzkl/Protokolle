from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

L = ufloat(3.53e-3, 0.03e-3)
C = ufloat(5.015e-9, 0.015e-9)
R = ufloat(271.6, 0.3)

print('q', 1/R * unp.sqrt(L/C))
print('R/L', R/L)
print('f_res', unp.sqrt(1/(L*C) - R**2/(2*L**2)))
print('f_1', R/(2*L) + unp.sqrt(R**2/(4*L**2) + 1/(L*C)))
print('f_2', -R/(2*L) + unp.sqrt(R**2/(4*L**2) + 1/(L*C)))
