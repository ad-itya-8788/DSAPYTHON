import matplotlib.pyplot as plt
values=[10,20,40]
name=['Category A','Category B','Category C']
plt.pie(values,labels=name,explode=[0,0,.03],autopct="%0.2f%%")
plt.title("Pie Demo Chart")
plt.show()