import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline
t = np.arange(0.0,2.0,0.01)
s = 1 + np.ln(2*np.pi*t)

plt.plot(t,s)
plt.show()
