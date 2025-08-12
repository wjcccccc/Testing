import numpy as np
import matplotlib.pyplot as plt

Vt = 0.7  
W = 10.0  
L_values = [0.8, 0.5, 0.25, 0.18, 0.13, 0.065, 0.028] 
Cox_u = 0.058  # Cox * u

VG = np.linspace(0, 5, 400)

for L in L_values:
    ID = np.piecewise(VG, [VG < Vt, VG >= Vt],
                      [0, lambda VG: 0.5 * Cox_u * W / L * ((VG - Vt) ** 2)])
    plt.semilogx(VG, ID, label=f'L={L}')

plt.axvline(x=Vt, color='r', linestyle='--', label='Threshold Voltage (Vth)')

plt.legend()
plt.title('PMOS Transfer Characteristic (ID-VG) for Different Channel Lengths')
plt.xlabel('Gate Voltage (VG)')
plt.ylabel('Drain Current (ID)')
plt.grid(True)
plt.show()