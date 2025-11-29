import numpy as np

a=np.array([1,2,3,4,5,6,3,7,8])

print(a)

z=a.reshape(3,3)
print(z)

x=z.flatten()
print(x)