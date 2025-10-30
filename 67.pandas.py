#dataframe.info():The dataframe.info() method in Pandas helps us in providing a concise summary of our DataFrame 
#and it quickly assesses its structure, identify issues like missing values and optimize memory usage.
import pandas as pd
df=pd.read_csv('66.nba.csv')
print(df.info())
print("_________________________________________________________________________________")

#1.Shortened Summary with verbose=False:By setting verbose=False we exclude detailed column information such as the
#number of non-null values which is useful when working with large datasets where we might not need all the details.
print(df.info(verbose=False))
print("_________________________________________________________________________________")

#2.Full Summary with Memory Usage:By setting memory_usage=True,the dataframe.info() method will provide an overview 
#of how much memory the DataFrame uses including both data and index memory usage.
print(df.info(memory_usage=True))
print("_________________________________________________________________________________")

# describe():describe() method generates a statistical summary
print(df.describe())
print("_________________________________________________________________________________")

#1.Customizing describe() with Percentiles:By passing a list of percentiles we can obtain more detailed insights 
#into our data’s distribution beyond the default 25th, 50th and 75th percentiles.
percentiles = [.20, .40, .60, .80]
include = ['object', 'float', 'int']
desc = df.describe(percentiles=percentiles, include=include)
print(desc)
print("_________________________________________________________________________________")

#2.Describing String (Object) Data:The describe() method also works with string data i.e object data type.When used 
# on string data, it provides different statistics such as the count of unique values, most frequent values etc.
desc=df['Name'].describe()
print(desc)
print("_________________________________________________________________________________")

# 3.Describing Specific Columns with describe():
salary_desc=df['Salary'].describe()
print(salary_desc)
print("_________________________________________________________________________________")

#4.Describing Data with include='all':By using the include='all' parameter we can generate a summary for all columns 
#in the DataFrame regardless of data type.
desc_all=df.describe(include='all')
print(desc_all)
print("_________________________________________________________________________________")

#COUNT VALUES IN PANDAS DATAFRAME
#1.Counting Unique Values in a Column
unique_names = df['Name'].nunique()
print(unique_names)
print("_________________________________________________________________________________")

#2.Counting Non-Null Values
non_null_ages = df['Age'].count()
print(non_null_ages)