# -*- coding: utf-8 -*-
"""
Magnitude and phase response of active filters

"""

# %% Init
import numpy as np
# https://docs.scipy.org/doc/scipy/reference/signal.html#
import scipy.signal as sig
import matplotlib.pyplot as plt

# %% Definition der TFs
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.tf2zpk.html#scipy.signal.tf2zpk
H0 = 1
Q = 10
f0 = 1e3
w0 = 2*np.pi*f0
f = np.logspace(2, 4, 400)

LPF = sig.lti([H0], [1/w0**2, 1/(w0*Q), 1])
w, magLPF, phaseLPF = LPF.bode(2*np.pi*f)

HPF = sig.lti([H0/w0**2, 0, 0], [1/w0**2, 1/(w0*Q), 1])
w, magHPF, phaseHPF = HPF.bode(2*np.pi*f)

BPF = sig.lti([-H0/w0, 0], [1/w0**2, 1/(w0*Q), 1])
w, magBPF, phaseBPF = BPF.bode(2*np.pi*f)

BSF = sig.lti([H0/w0**2, 0, H0], [1/w0**2, 1/(w0*Q), 1])
w, magBSF, phaseBSF = BSF.bode(2*np.pi*f)

# %% Erzeugen des Bode-Diagramms
plt.subplot(2, 1, 1)
plt.semilogx(f, magLPF, label='LPF')
plt.semilogx(f, magHPF, label='HPF')
plt.semilogx(f, magBPF, label='BPF')
plt.semilogx(f, magBSF, label='BSF')
plt.ylabel(r'$\vert H_v \vert$/dB')
plt.grid()
plt.legend()
plt.subplot(2, 1, 2)
plt.semilogx(f, phaseLPF, label='LPF')
plt.semilogx(f, phaseHPF, label='HPF')
plt.semilogx(f, phaseBPF, label='BPF')
plt.semilogx(f, phaseBSF, label='BSF')
plt.ylabel(r'$arg(H_v)$/deg')
plt.xlabel('f/Hz')
plt.grid()
plt.show()
