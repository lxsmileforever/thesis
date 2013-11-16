import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0,2*np.pi+np.pi/4,2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x,y,s=0)
xnew = np.arange(0,3*np.pi,np.pi/50)
ynew = interpolate.splev(xnew,tck,der=0)

plt.figure()
plt.plot(xnew,ynew,'ro')
plt.show()