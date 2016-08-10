#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from spectra.spectrum import Spectrum

inpfname = 'dir/to/datafile'

guess = [ 
        [Area, FWHM, omega_0], 
        [Area, FWHM, omega_0], 
        ...
        [offset]
     ]


cols = np.genfromtxt(inpfname, unpack=True) #delimiter=",", 
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

spectrum = Spectrum(cols[0],cols[1])
spectrum.gausfit(guess)
print('Results of fitted peak, ', spectrum.gfit_oup)
print('Correlation coefficient, ', spectrum.corr_coef[0,1])

ax.plot(spectrum.x, spectrum.y)
spectrum.plot_gfit(ax, pltguess=True)

plt.show()


