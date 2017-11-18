from uncertainties import ufloat
import numpy as np

V_k = ufloat(5.0e-5, 1.1e-05)
V_r = ufloat(0.000219, 0.000033)
V_a = ufloat(4.3e-5, 0.5e-05)
V_b = ufloat(5.8e-5, 0.9e-05)
V_g = ufloat(0.00047, 0.00004)

print('m_k=', (V_k*341.2e-3)/V_g)
print('m_r=', (V_r*341.2e-3)/V_g)
print('m_a=', (V_a*341.2e-3)/V_g)
print('m_b=', (V_b*341.2e-3)/V_g)
