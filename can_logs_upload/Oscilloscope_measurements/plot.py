
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

data = np.genfromtxt('RigolDS0.csv', delimiter=',', skip_header=1,
                     skip_footer=0, names=['x', 'ch1', 'ch2', 'ch3'])
                     
fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Zoe Analog Signals")    
ax1.set_xlabel('Time [S]')
ax1.set_ylabel('Voltage [V]')
               
ax1.plot(data['x'], data['ch1'], color='y', label='CH1')
ax1.plot(data['x'], data['ch2'], color='b', label='CH2')
ax1.plot(data['x'], data['ch3'], color='r', label='CH3')

plt.show()
