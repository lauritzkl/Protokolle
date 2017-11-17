from uncertainties import ufloat
import numpy as np

D = ufloat(2.388e-2, 0.039e-2)
I = ufloat(2.154e-3, 0.414e-3)
T = ufloat(1.562, 0.048)
T_2 = ufloat(2.244, 0.007)
T_3 = ufloat(1.362, 0.032)
T_4 = ufloat(0.514, 0.062)


print('I_k=', repr((D/(2*np.pi)**2)*T**2 ))
print('I_z=', repr(((D/(2*np.pi)**2)*T_2**2) -I))
print('I_p1=', repr((D/(2*np.pi)**2)*T_3**2))
print('I_p2=', repr((D/(2*np.pi)**2)*T_4**2 ))
