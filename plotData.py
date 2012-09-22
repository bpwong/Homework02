#/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
'''
    plotData generates a plot using the provided data files:
    ny_temps.txt, yahoo_data.txt, google_data.txt
    
    An image of the plot generated can be found at NY_Google_Yahoo.png
'''

# Read in data from text file
dt = [('date',np.int32),('val',np.int32)]
goog = np.loadtxt('txt/google_data.txt',dt,skiprows=1)
ny = np.loadtxt('txt/ny_temps.txt',dt,skiprows=1)
yahoo = np.loadtxt('txt/yahoo_data.txt',dt, skiprows=1)

f, ax1 = plt.subplots(1,1)
ax2 = ax1.twinx() 
ax2.set_ylim([-150,100])

ln1 = ax1.plot(goog['date'],goog['val'], linewidth=2,label='Google Stock Value')
ln2 = ax2.plot(ny['date'],ny['val'], 'r--', linewidth=2, label = 'NY Mon. High Temp')
ln3 = ax1.plot(yahoo['date'],yahoo['val'], c='purple',linewidth=2,label='Yahoo! Stock Value')

# usetex demo: http://matplotlib.org/examples/pylab_examples/usetex_demo.html
rc('text', usetex = True)
plt.title(r'\bf{New York, Temperature, Google, and Yahoo!}',fontsize=20)

lns = ln3+ln1+ln2
labs = [l.get_label() for l in lns]
ax1.legend(lns,labs,loc='center left',frameon=False,prop={'size':11})

ax1.set_xlabel('Date (MJD)',fontsize=14)
ax1.set_ylabel('Value (Dollars)',fontsize=14)
ax1.minorticks_on()
ax1.tick_params(labelsize=10)
ax1.set_ylim(auto=True)
ax1.xaxis.tick_bottom()
#ax1.splines[''].set_linewidth(10)
#ax1.set_linewidth(4)

ax2.set_ylabel('Temperature ($\degree$F)',fontsize=14)
ax2.minorticks_on()
ax2.tick_params(labelsize=10)
ax2.autoscale(axis='x',tight=True)
ax2.set_xlim(48800,55600)
ax2.xaxis.tick_bottom()

plt.show()
