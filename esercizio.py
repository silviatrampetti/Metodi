import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2,10)
y = np.array([1,2,5,6,3,4,5,6])

plt.plot(x,y,'o-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
