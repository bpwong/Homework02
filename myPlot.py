#/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
'''
    myPlot generates plots in Python that have been originally done in MATLAB.
'''

# Read in data from text file
dt = [('measured',np.float64),('reference',np.float64)]
temps = np.loadtxt('USB-TEMP-EPCOS-Calib-Test - 2012 09 21_01.txt',dt)
title = 'Temperature Measurements'

# Generate time
t = [x * 0.5 for x in range(0, len(temps['reference']))]

# Generate Coefficients using Least Squares
A = np.array([temps['reference'], np.ones(len(temps['reference']))])
coef = np.linalg.lstsq(A.T,temps['measured'])[0]
range = np.linspace(min(temps['reference']), max(temps['reference']))

f, (ax1, ax2) = plt.subplots(1,2)

# Plot first subplot
ax1.plot(temps['reference'],temps['measured'],'x',c='b')
fit = ax1.plot(range,coef[1] + coef[0]*range)
plt.setp(fit,linewidth=2,c='g')
ax1.set_xlabel('$T_{thermocouple}$')
ax1.set_ylabel('$T_{thermistor}$')

# Plot second subplot
ax2.plot(t,temps['reference'],label='$T_{thermocouple}$')
ax2.plot(t,temps['measured'],label='$T_{thermistor}$')
ax2.legend(loc='best')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('T (C)')

# Show the plot
plt.show()
