import numpy as np 
import matplotlib.pyplot as plt
# x = np.linspace(0, 2*np.pi, 500)
# y = np.sin(x)
# plt.plot(y)
# plt.show()

fig, axes = plt.subplots(nrows=4)

def sine_function(idx,input):
    y = np.sin(input)
    axes[idx].plot(input, y)

x = np.linspace(0, 2*np.pi, 500)
a = np.linspace(0, 3*np.pi, 500)
b = np.linspace(0, 4*np.pi, 500)
c = np.linspace(0, 5*np.pi, 500)

sine_function(0,x)
sine_function(1,a)
sine_function(2,b)
sine_function(3,c)

plt.show()
