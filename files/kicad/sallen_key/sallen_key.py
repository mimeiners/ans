import ltspice
import matplotlib.pyplot as plt
import numpy as np
import os

l = ltspice.Ltspice(os.path.dirname(__file__)+'/sallen_key.raw') 
# Make sure that the .raw file is located in the correct path
l.parse() 

# %% Get data
freq = l.get_frequency()
V_bp = l.get_data('V(/bp)')
V_hp = l.get_data('V(/hp)')

# %% Plot
plt.semilogx(freq, 20*np.log10(np.abs(V_bp)))
plt.semilogx(freq, 20*np.log10(np.abs(V_hp)))
plt.grid()
plt.xlabel("Frequenz f/Hz")
plt.ylabel(r'$H_v$/dB')
plt.show()
