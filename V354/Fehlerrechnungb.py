from uncertainties import ufloat
import numpy as np
import uncertainties.unumpy as unp

L = ufloat(3.53e-3, 0.03e-3)
C = ufloat(5.015e-9, 0.015e-9)

print('R_ap=', unp.sqrt((4*L)/C))
