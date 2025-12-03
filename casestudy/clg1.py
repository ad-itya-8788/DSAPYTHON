import pandas as pd
import numpy as np

#creating a pandas series from a list
data=[1,2,3,4,5]
series = pd.Series(data)

#creating a pandas series with specific index
index = ['a','b','c','d','e']
series_with_index= pd.Series(data,index=index)

#creating a pandas series from dictionaries
data_dic={'a':1,'b':2,'c':3,'d':4}
series_from_dict=pd.Series(data_dic)

#accessing data in a series
print(series[2])      #accessing element at index 2
print(series_with_index['b'])  #accessing element with index b


#Operations and Transformation in Pandas series
#element wise addition
result = series + series_with_index
print(result)


