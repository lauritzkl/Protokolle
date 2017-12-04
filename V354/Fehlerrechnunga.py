from uncertainties import ufloat
import numpy as np

L = ufloat(3.53e-3, 0.03e-3)
b = ufloat(11450.5, 96.46)
d = ufloat(12049.8, 212.47)

print('R_1=', 2*b*L)
print('R_2=', 2*d*L)
print('T_ex1=', 1/b)
print('T_ex2=', 1/d)
