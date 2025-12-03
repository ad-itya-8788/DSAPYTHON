import matplotlib.pyplot as plt

x=[1,3,4,5]
y=[12,34,55,66]

plt.plot(x,y,linestyle='--',marker='*',label="This is Demo")
plt.legend()
plt.title("Demo Graph")
plt.xlabel("This is x label")
plt.ylabel("This is y Label")
plt.grid(True)
plt.show()
