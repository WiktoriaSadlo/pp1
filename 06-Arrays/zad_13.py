import matplotlib.pyplot as plt
import numpy as np

x=np.array(["car","public transport","bike","on foot"])
y=np.array([23,19,32,7])

plt.bar(x,y, width=0.5)
plt.title("Transport")
plt.ylabel("People")


plt.show()