import pandas as pd
data = {'a':10,'b':20,'c':30,'d':40,'e':50}
series = pd.Series(data)
print(series)

#select elements greater than 30
selected_greater_than_30 = series[series>30]
print("\nSelected_greater_than_30:\n", selected_greater_than_30)

#select elements equal to 20
selected_equal_to_20 = series[series==20]
print("\nSelected_equal_to_20:\n", selected_equal_to_20)

#select elements not equal to 40
selected_not_equal_to_40 = series[series!=40]
print("\nSelected_not_equal_to_40:\n", selected_not_equal_to_40)

#select elements less than 30
selected_less_than_30 = series[series<30]
print("\nSelected_less_than_30:\n", selected_less_than_30)

#select elements based on multiple conditions
selected_multiple_conditions = series[(series>20) & (series<50)]
print("\nSelected_multiple_conditions:\n", selected_multiple_conditions)

#select elements based on list of values
selected_by_list = series[series.isin([20,40,60,80,100])]
print("\nSelected_by_list:\n", selected_by_list)

#select elements using string methods(if applicable)
string_series = pd.Series(['apple','banana','cherry','date','elderberry'])
selected_by_string_method = string_series.str.startswith('b')
print("\nselected by string method")
print(selected_by_string_method)
selected_by_string_method1 = string_series[string_series.str.startswith('b')]
print("\nselected by string method1")
print(selected_by_string_method1)

#Query based on index labels
#loc (Label-based indexing)
#selects data by labels (names) of rows and columns
selected_by_index_labels = series.loc[['a','b','c']]
print("\nSelected_by_index_labels:\n", selected_by_index_labels)

#Query based on numeric positions
#iloc (Integer-Location-based indexing)
#Selects data by integer positions of rows and columns
selected_by_numeric_positions = series.iloc[1:4]
print("\nSelected_by_numeric_positions:\n", selected_by_numeric_positions)

# Creating a DataFrame from a dictionary
data_dict = {'Name': ['Richa', 'Jemimah', 'Amanjot'],
             'Age': [19,35,22],
             'Salary': [50000, 60000, 45000]}
df_dict = pd.DataFrame(data_dict)
print(df_dict)

#Creating a DataFrame from Lists
data_list = [['Harman', 25, 50000],['Kriti',26, 60000], ['Shruti', 20, 70000]]

#defining column names
columns = ['Name', 'Age', 'Salary']

df_list = pd.DataFrame(data_list, columns=columns)
print(df_list)
print(df_list['Name'])
print(df_list['Age'])
print(df_list['Salary'])

data_array = np.array([['Pratik', 25, 50000], ['Shradha', 24, 60000], ['Gautami',20, 70000]])
df_array = pd.DataFrame(data_array, columns=columns)
print(df_array)

#creating a DataFrame from a CSV file
#df_csv = pd.read_csv('HousePrices.csv')
#print(df_csv)

#Creating a sample DataFrame
data = {'Column_name': [5,15,8],
        'Column1': [10,20,30],
        'Column2': [20,40,60],
        'Another_column': [25,35,45]}
df = pd.DataFrame(data)

#Accessing a single column
column_data = df['Column_name']
print("Single column: ")
print(column_data)

#Accessing multiple columns
selected_columns = df[['Column1', 'Column2']]
print("Multiple columns: ")
print(selected_columns)

#Accessing a specific row by index
row_data = df.iloc[0]
print("\nSpecific row: ")
print(row_data)

#Accessing rows based on a condition
filtered_rows = df[df['Column_name'] > 10]
print("\nFiltered rows: ")
print(filtered_rows)

#Accessing a single cell by label
value = df.at[0,'Column_name']
print("\nSingle cell by label:")
print(value)

#Accessing a single cell by position
value = df.iat[0,1]   #Row0, Column1
print("\nSingle cells by label:")
print(value)

selected_data= df.loc[0, 'Column_name']
print("\nData using .loc:")
print(selected_data)

#Conditional access
selected_data = df[df['Column_name'] > 10]['Another_column']
print("\nConditional access:")
print(selected_data)

#display the first 2 rows
print("First 2 rows: ")
print(df.head(2))

#display the last row
print("\nLast row:")
print(df.tail(1))

#provide a comprehensive summary of the DataFrame
print("\nDataFrame summary:")
df.info()
df.describe()

#print("\n DataFrame dimension
print(df.shape)


#calculate mean,median, and standard deviation
mean_value = df.mean()
print("\nMean of column values:")
print(mean_value)

median_value = df.median()
print("\nMedian of column values:")
print(median_value)

std_deviation = df.std()
print("\nStandard Deviation of column values:")
print(std_deviation)
