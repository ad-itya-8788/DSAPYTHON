from operator import lt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[1,2,3,4]
y=[1,2,3,4]

plt.title("Heading",color='Red',fontsize=10)
plt.plot(x,y,'r*--')
plt.xlabel("X-Axis",color='red',fontsize=10)
plt.ylabel("y-Axis",color='red',fontsize=10)
plt.legend(['Single Element'])
plt.savefig("graph.png")
plt.show()
