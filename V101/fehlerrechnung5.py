from uncertainties import ufloat
import numpy as np

m_k = ufloat(0.036, 0.009)
m_r = ufloat(0.159, 0.028)
m_a = ufloat(0.031, 0.004)
m_b = ufloat(0.042, 0.007)
D_k = ufloat(3.0225e-2, 0.3186e-2)
D_r = ufloat(4.817e-2, 0.364e-2)
D_a = ufloat(1.793e-2, 0.101e-2)
D_b = ufloat(1.97e-2, 0.15e-2)

print('I_k=', (m_k*D_k**2)/8)
print('I_r=', (m_r*D_r**2)/8)
print('I_a=', (m_a*(D_a**2/16)+((17.13e-2)**2/12))+(m_a*((D_r/2) + (17.13e-2/2))**2))
print('I_b=', ((m_b*D_b**2)/8)+ (m_b*(D_b/2)**2))
print((m_k*D_k**2)/8 + (m_r*D_r**2)/8 + 2*((m_a*(D_a**2/16)+((17.13e-2)**2/12))+(m_a*((D_r/2) + (17.13e-2/2))**2))
+ 2*(((m_b*D_b**2)/8)+ (m_b*(D_b/2)**2)))

print('I_a2=', ((m_a*D_a**2)/8) + (m_a*((D_r/2)+(D_a/2))**2))
print((m_k*D_k**2)/8 + (m_r*D_r**2)/8 + 2*(((m_a*D_a**2)/8) + (m_a*((D_r/2)+(D_a/2))**2))
+ 2*(((m_b*D_b**2)/8)+ (m_b*(D_b/2)**2)))
