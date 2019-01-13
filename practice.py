import numpy as np 
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def sine_function(end):
    x = np.linspace(0, end*np.pi, 500)
    y = np.sin(x+0.5*end*np.pi)
    ax.plot(x, y, label='foo ' + str(end))

sine_function(2)
sine_function(3)
sine_function(4)
sine_function(5)

ax.legend(loc='best')

plt.show()
