import numpy as np
from uncertainties import ufloat

R_a = ufloat(16.82, 0.45)
R_c1 = ufloat(117.95, 1.88)
R_c2 = ufloat(115.21, 2.71)
U_k = 1.65
R_v = 10**7

print('a=', U_k*R_a/R_v)
print('a1=', R_a/R_v)
print('b=', U_k*R_c1/R_v)
print('b1=', R_c1/R_v)
print('c=', U_k*R_c2/R_v)
print('c1=', R_c2/R_v)
