# Data Structures in Pandas Library:
#1.Pandas Series:A Pandas Series is one-dimensional labeled array capable of holding data of any type(integer,string,
#float, Python objects etc.). The axis labels are collectively called indexes.Pandas Series is created by loading the 
#datasets from existing storage which can be a SQL database, a CSV file or an Excel file. It can be created from
#lists, dictionaries, scalar values, etc.
import pandas as pd 
import numpy as np

ser = pd.Series() 
print("Pandas Series: ", ser) 
data = np.array(['S','A','R','F','A','R','A','J','S','H','A','I','K','H'])  
ser = pd.Series(data) 
print("Pandas Series:\n", ser)
print("_________________________________________________________________________________")

# ACCESSING ELEMENT OF SERIES:
#(1)Position-based Indexing:In order to access the series element refers to the index number.Use the index operator
#[]to access an element in a series. The index must be an integer.In order to access multiple elements from a series 
#we use Slice operation.
print(ser[:5])
print("_________________________________________________________________________________")

#(2)Label-based Indexing:In order to access an element from series,we have to set values by index label.A Series is 
#like a fixed-size dictionary in that we can get and set values by index label.
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22,23])
print(ser[16])
print("_________________________________________________________________________________")

#INDEXING AND SELECTING DATA
df=pd.read_csv("66.nba.csv")
ser=pd.Series(df['Name'])
data=ser.head(10)
print(data)
print("_________________________________________________________________________________")

#1.Indexing a Series using .loc[]:This function selects data by refering the explicit index.The df.loc indexer 
#selects data in a different way than just the indexing operator. It can select subsets of data.
print(data.loc[3:6])
print("_________________________________________________________________________________")

#2.Indexing a Series using .iloc[]:.iloc[] function allows us to retrieve data by position.In order to do that 
#we’ll need to specify the positions of the data that we want. The df.iloc indexer is very similar to df.loc but 
#only uses integer locations to make its selections.
print(data.iloc[3:6])
print("_________________________________________________________________________________")

#BINARY OPERATION ON PANDAS SERIES:Pandas allows performing binary operations on Series,such as addition,subtraction, 
#multiplication and division.These operations can be performed using functions like .add(),.sub(),.mul() and .div()
ser1=pd.Series([1,2,3],index=['a','b','c'])
ser2=pd.Series([9,7,5],index=['a','b','c'])
df_sum=ser1.add(ser2)
print(df_sum)
print("_________________________________________________________________________________")

#CONVERSION OPERATION ON SERIES:Conversion operations allow transforming data types within a Series.In order to 
#perform conversion operation we have various function which help in conversion like .astype(), .tolist() etc
ser=df_sum.astype(float)
print(ser)
print("_________________________________________________________________________________")

#2.Pandas DataFrame:Pandas DataFrame is a two-dimensional data structure with labeled axes(rows and columns).It is
#created by loading the datasets from existing storage which can be a SQL database, a CSV file or an Excel file.It
#can be created from lists, dictionaries, a list of dictionaries etc.
df = pd.DataFrame() 
print(df)
lst = ['Pandas', 'NumPy', 'Matplotlib', 'Random', 'Request', 'Threadig', 'Scikit-learn'] 
df = pd.DataFrame(lst) 
print(df)
print("_________________________________________________________________________________")

data={'Name':['rohit','pratik','prathmesh','anwar'],
      'age':[43,46,66,36],
      'Address':['mirjapur','badlapur', 'kolhapur', 'Allahabad', ],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
print(df)
print("_________________________________________________________________________________")

#WORKING WITH COLUMN AND ROWS IN PANDAS DATAFRAME
#1.column selection
print(df[['Name','Qualification']])
print("_________________________________________________________________________________")

# 2.row selection
data=pd.read_csv('66.nba.csv',index_col='Name')
first=data.loc['Avery Bradley']
print(first)
print("_________________________________________________________________________________")

# 3.Indexing a Dataframe using indexing operator [] 
second=data['Age']
print(second)
print("_________________________________________________________________________________")

third=data.iloc[3]
print(third)
print("_________________________________________________________________________________")

#WORKING WITH MISSING VALUES
#1.Checking for Missing Values using isnull() and notnull()
# i]isnull(): It returns True for NaN (missing) values and False otherwise.
# ii]notnull(): It returns the opposite, True for non-missing values and False for NaN values
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
df=pd.DataFrame(dict)
print(df.isnull())
print("_________________________________________________________________________________")

#2.Filling Missing Values using fillna(), replace() and interpolate():All these function help in filling a null 
#values in datasets of a DataFrame.Interpolate() function is used to fill NA values in the dataframe but it uses
#various interpolation technique to fill the missing values rather than hard-coding the value.
print(df.fillna(0))
print("_________________________________________________________________________________")

#3.Dropping Missing Values using dropna():If we want to remove rows or columns with missing data we can use the 
#dropna() method. This method is flexible which allows us to drop rows or columns depending on the configuration.
print(df.dropna())
print("_________________________________________________________________________________")

#ITERATING OVER ROWS AND COLUMNS:Iteration refers to the process of accessing each item one at a time.
# 1. Iterating Over Rows
        # iteritems()
        # iterrows()
        # itertuples()
for i,j in df.iterrows():
    print(i, j)
    print()
print("_________________________________________________________________________________")

for i in df.itertuples():
    print(i,j)
    print()
print("_________________________________________________________________________________")

for item in df.items():
    print(item)
    print()
print("_________________________________________________________________________________")

#2.Iterating Over Columns:
columns=list(df)

for i in columns:
    print(df[i][2])
print("_________________________________________________________________________________")

#READING DATAFRAME
#1.viewing rows in dataframe:    
#     head(n): Displaying the First Few Rows
#     tail(n): Displaying the Last Few Rows
data={'Name':['rohit','pratik','prathmesh','anwar'],
      'age':[43,46,66,36],
      'Address':['mirjapur','badlapur', 'kolhapur', 'Allahabad', ],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
print(df.head(3))
print(df.tail(2))
print("_________________________________________________________________________________")

#2.Exploring Columns of the dataset
print(df.columns)
print("_________________________________________________________________________________")

#3. Checking Data Types with dtype
print(df.dtypes)
print("_________________________________________________________________________________")

#4.Generating Descriptive Statistics with describe()
print(df.describe())
print("_________________________________________________________________________________")

#5.Finding Unique Values in a Column
print(df["Address"].unique())
print("_________________________________________________________________________________")

#6.Filtering Rows (Conditional Filtering)
print(df[df["age"] > 30])   
print("_________________________________________________________________________________")

print(df[(df["age"] > 30) | (df["Address"] == "kolhapur")])
print("_________________________________________________________________________________")

#7.Updating a Single Value: 
df.loc[df['Name'] == 'rohit', 'age'] = 70
print(df)
print("_________________________________________________________________________________")

#8.Updating an Entire Column:
df['Address']=['palus','santgaon','sangli','vita']
print(df)
print("_________________________________________________________________________________")

#9.Delete a Column
df = df.drop('Qualification', axis=1)
print(df)
print("_________________________________________________________________________________")

#10.Delete a Row
df = df.drop(2, axis=0) 
print(df)
print("_________________________________________________________________________________")

#11.Delete Rows Based on Condition:
df = df[df['age'] != 36]
print(df)
print("_________________________________________________________________________________")

#12.Delete entire dataset
del df
print(df)