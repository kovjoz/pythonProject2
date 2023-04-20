import pandas as pd

df1 = pd.read_csv("C:\\Users\\jkovacs\\Desktop\\house-prices-advanced-regression-techniques\\train.csv", index_col='Id')
"""
print("*** Row:")
print(df1.iloc[19])
print("*** Column:")
print(df1.iloc[:, 18])"""

#print(df1.loc[:, ['YearBuilt', 'GarageYrBlt']])
#print(df1.loc[df1.GarageYrBlt < df1.YearBuilt])
#x = df1.loc[df1.GarageYrBlt < df1.YearBuilt]
#print(x.loc[:, ['YearBuilt', 'GarageYrBlt']])

#print((df1.loc[df1.GarageYrBlt < df1.YearBuilt])
#      .loc[:, ['YearBuilt', 'GarageYrBlt']])

#print(df1.loc[df1.Exterior2nd == "Wd Shng"])
