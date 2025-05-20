#!/usr/bin/env python
# coding: utf-8
"""Post-processing of ltspice data"""

import ltspice
import matplotlib.pyplot as plt

# %% Load RAW LTSpice into python workspace
file = "./Universal_Biquad_tl082.raw"
raw = ltspice.Ltspice(file)
raw.parse()

# %% Extract voltages and time
t = raw.get_time()
vin = raw.get_data('V(vin)')
vbp = raw.get_data('V(vbp)')

# %% Plots
plt.plot(t, vin, label=r'$v_{in}(t)$')
plt.plot(t, vbp, label=r'$v_{bp}(t)$')
plt.legend()
plt.xlabel('Time t in s')
plt.ylabel('Voltages in V')
plt.grid()
plt.show()
