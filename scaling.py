import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.style.use('dark_background')

x = [10,20,100]
y = [9.12,31.69,777.96]

def exponenial_func(x, a, b, c):
    return a*np.exp(b*x)+c

popt, pcov = curve_fit(exponenial_func, x, y, p0=(1, 1e-6, 1))

xx = np.linspace(10, 100, 10)
yy = exponenial_func(xx, *popt)
qq = xx*2

plt.plot(xx,yy,color='r',label='Other Methods')
plt.plot(xx,qq,color='y',label='Quantum Democratica')
plt.xlabel('Number of Voters [Millions]')
plt.ylabel('Computation Time [scaled]')
plt.legend()
plt.savefig('scaling.png')
