import numpy as np
import matplotlib.pyplot as plt


Vt = 0.7       
W = 10         
L_values = [0.8, 0.5, 0.25, 0.18, 0.13, 0.065, 0.028]  
Cox_mu = 0.058 

VSD = np.linspace(0, 5, 100)


VSG = 1.0 

for L in L_values:
    Kn = Cox_mu * (W / L)  
    ID_saturated = np.where(VSD > (VSG - Vt), 0.5 * Kn * (VSG - Vt)**2, Kn*((VSG-Vt)*VSD-0.5*VSD*VSD))
    plt.plot(VSD, ID_saturated, label=f'L = {L}')

plt.title('PMOS Output Characteristics')
plt.xlabel('VSD (V)')
plt.ylabel('ID (mA)')
plt.legend()
plt.grid(True)
plt.show()
