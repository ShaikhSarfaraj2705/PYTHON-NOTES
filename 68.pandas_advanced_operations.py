import pandas as pd
df=pd.read_csv("66.nba.csv")
bool_series=pd.isnull(df["College"])
missing_gender_data=df[bool_series]
print(missing_gender_data)
print("_________________________________________________________________________________")

dublicates=df[df.duplicated()]
print(dublicates)
bool_series = df["Name"].duplicated()
print(bool_series)