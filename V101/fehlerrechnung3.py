from uncertainties import ufloat
import numpy as np

D_k = ufloat(3.0225e-2, 0.3186e-2)
D_r = ufloat(4.817e-2, 0.364e-2)
D_a = ufloat(1.793e-2, 0.101e-2)
D_b = ufloat(1.97e-2, 0.15e-2)

print('V_k=', (np.pi/4) * D_k**2 * 7e-2)
print('V_r=', (np.pi/4) * D_r**2 * 12.03e-2)
print('V_a=', (np.pi/4) * D_a**2 * 17.13e-2)
print('V_b=', (np.pi/4) * D_b**2 * 18.99e-2)
print((np.pi/4) * D_k**2 * 7e-2 + (np.pi/4) * D_r**2 * 12.03e-2 + 2*(np.pi/4) * D_a**2 * 17.13e-2+
2*(np.pi/4) * D_b**2 * 18.99e-2)
