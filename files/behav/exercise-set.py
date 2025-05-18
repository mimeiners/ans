#!/usr/bin/env python

""" Exercise Set """

# Python scipy.signal IIR Filter Design
# http://www.dsprelated.com/showarticle/164.php
# Posted by Christopher Felton on May 13 2012
import numpy as np
import scipy.signal as sig
from scipy.signal import filter_design as fd
import matplotlib.pyplot as plt

# Design a Chebychev-II lowpass filter
#
# a)
# Filter spcification
wp = 2*np.pi*5E6   # 5 MHz passband edge
ws = 2*np.pi*10E6  # 10 MHz stopband edge
Rp = 2             # Define the passband edge at -2dB
Rs = 60            # Specify 60dB stopband attenuation

# Find the required Chebyshev2 filter order for the given specs
# [N, ws_new] = cheb2ord(wp, ws, Rp, Rs, 's')
[N, ws_new] = fd.cheb2ord(wp, ws, Rp, Rs, analog='True')
print('The required filter order is ', N)

# b)
[z, p, k] = fd.cheby2(N, Rs, ws_new, btype='lowpass',
                                     analog='True', output='zpk')
sys = sig.lti(z, p, k)
f = np.logspace(5, 9, 3000)
w, mag, phase = sys.bode(2*np.pi*f)
# f = w/(2*np.pi)

# Unwrap the phase to make the jumps consistent and shift to 0 at w=0
angle = np.rad2deg(np.unwrap(np.deg2rad(phase)))
angle = angle - angle[1]


# Generate the magnitude plot with annotation, phase, and group delay plots
mindB = -80
maxdB = 5
plt.figure(1)
plt.subplot(2, 1, 1)
plt.semilogx(f, mag)

# plt.line([np.min(f) 5e6], [-2 -2])
# plt.line([5e6 5e6], [mindB -2])
# plt.line([np.min(f) 10e6], [0 0])
# plt.line([10e6 10e6], [0 -60])
# plt.line([10e6 f[-1]], [-60 -60])

plt.grid()
plt.xlabel('Frequency f/Hz')
plt.ylabel('Magnitude A/dB')
plt.axis([np.min(f), np.max(f), mindB, maxdB])

plt.subplot(2, 1, 2)
plt.semilogx(f, angle)
plt.grid()
plt.xlabel('Frequency f/Hz')
plt.ylabel('Phase phi/deg')
plt.axis([np.min(f), np.max(f), -500, 100])
plt.show()


plt.figure(2)
Tgd = -1e9*np.diff(2*np.pi*angle/360)/np.diff(w)
Tgd[np.abs(Tgd) > 500] = np.NaN  # Eliminate discontinuities
plt.semilogx(f[1:], Tgd)
plt.xlabel('Frequency f/Hz')
plt.ylabel('Group Delay Tgd/ns')
plt.axis([np.min(f), np.max(f), -50, 250])
plt.grid()
plt.show()

# c)
plt.figure(3)
w_limit = 3E8
plt.plot(p.real, p.imag, 'rx')
plt.plot(z.real, z.imag, 'bo')
plt.axis([-w_limit, w_limit, -w_limit, w_limit])
plt.grid()
plt.xlabel(r'$\sigma$')
plt.ylabel(r'$j\omega$')
plt.title('Complex s-plane')
plt.show()

# Find the angle of each pole w.r.t. the negative real axis to get Q
alphas = np.arccos(-np.real(p)/np.abs(p))
Qp = 1.0/(2*np.cos(alphas))
wp_locations = np.abs(p)
# print(' poles [*1e7] wp [*1e7] Qp\n\n')
print(p)
print(wp_locations)
print(Qp)


# d)
# Check the Butterworth filter order required for the same specs.
[N_butter, wn_butter] = fd.buttord(wp, ws, Rp, Rs, analog='True')
print('The required Butterworth filter order is ', N_butter)


# e)
plt.figure(4)
plt.semilogx(f, mag)
plt.xlabel('Frequency f/Hz')
plt.ylabel('Magnitude A/dB')
plt.axis([np.min(f), np.max(f), mindB, maxdB])
plt.grid()

# From manually tweaking the passband back to 2dB at 5MHz using Rs
[N_butter, wn_butter] = fd.buttord(5e6, 10e6, 2, 33.78, analog='True')
[z_butter, p_butter, k_butter] = fd.butter(N_butter, wn_butter,
                                           btype='lowpass', analog='True',
                                           output='zpk')
sys_butter = sig.lti(z_butter, p_butter, k_butter)
[w_butter, mag_butter, phase_butter] = sys_butter.bode(2*np.pi*f)
plt.semilogx(w_butter, mag_butter)
plt.legend(('Cheby2 n=6', 'Butterworth n=6'))
plt.show()

alphas_butter = np.arccos(-np.real(p_butter)/np.abs(p_butter))
Qp_butter = 1/(2*np.cos(alphas_butter))
wp_locations_butter = np.abs(p_butter)
