#/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
'''
    plotData generates a plot using the provided data files:
    ny_temps.txt, yahoo_data.txt, google_data.txt
'''

# Read in data from text file
dt = [('date',np.int32),('val',np.int32)]
goog = np.loadtxt('txt/google_data.txt',dt,skiprows=1)
ny = np.loadtxt('txt/ny_temps.txt',dt,skiprows=1)
yahoo = np.loadtxt('txt/yahoo_data.txt',dt, skiprows=1)

f, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx() 
ax2.set_ylim([-150,100])

ln1 = ax1.plot(goog['date'],goog['val'], label='Google Stock Value')
ln2 = ax2.plot(ny['date'],ny['val'], '--', c='r',label = 'NY Mon. High Temp')
ln3 = ax1.plot(yahoo['date'],yahoo['val'], c='purple',label='Yahoo! Stock Value')

plt.title('New York Temperature, Google, and Yahoo!')

lns = ln3+ln1+ln2
labs = [l.get_label() for l in lns]
ax1.legend(lns,labs,loc='center left',frameon=False,prop={'size':10})

ax1.set_xlabel('Date (MJD)')
ax1.set_ylabel('Value (Dollars)')
ax1.minorticks_on()
ax1.tick_params(labelsize=10)
ax1.set_ylim(auto=True)
ax1.xaxis.tick_bottom()
#ax1.splines[''].set_linewidth(10)
#ax1.set_linewidth(4)

ax2.set_ylabel('Temperature ($\degree$F)')
ax2.minorticks_on()
ax2.tick_params(labelsize=10)
ax2.autoscale(axis='x',tight=True)
ax2.set_xlim(48800,55600)
ax2.xaxis.tick_bottom()
comm = '''
# Generate time
t = [x * 0.5 for x in range(0, len(temps['reference']))]

# Generate Coefficients using Least Squares
A = np.array([temps['reference'], np.ones(len(temps['reference']))])
coef = np.linalg.lstsq(A.T,temps['measured'])[0]
range = np.linspace(min(temps['reference']), max(temps['reference']))



# Plot first subplot
ax1.plot(temps['reference'],temps['measured'],'x',c='b')
fit = ax1.plot(range,coef[1] + coef[0]*range)
plt.setp(fit,linewidth=2,c='g')
ax1.set_xlabel('T$_{thermocouple}$')
ax1.set_ylabel('T$_{thermistor}$')

# Plot second subplot
ax2.plot(t,temps['reference'],label='T$_{thermocouple}$')
ax2.plot(t,temps['measured'],label='T$_{thermistor}$')
ax2.legend(loc='best')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('T (C)')

# Show the plot
    '''
plt.show()
