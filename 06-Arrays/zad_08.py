import matplotlib.pyplot as plt
import numpy as np

#x=[i for i in range(0,10,2)]
#y=[i**3 for i in range(0,10,2)]
theta = np.linspace(0, 2 * np.pi, 100)
x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)


plt.plot(x,y, color = "#c920a2")

plt.xlabel("oś X")
plt.ylabel("oś Y")
plt.show()