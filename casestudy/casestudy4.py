import pandas as pd
x=[10,20,30,50]
name=['Aditya','sham','Ram','Ganesh']
score=pd.Series(x,index=name)
print(score)