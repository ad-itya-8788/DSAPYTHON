import matplotlib.pyplot as plt
import numpy as np

test=np.random.normal(200,300,400)
test2=np.random.normal(100,200,400)
test3=np.random.normal(10,20,40)
main=[test,test2,test3]
plt.boxplot(main)
plt.show()
