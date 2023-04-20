import pandas as pd

titanic = pd.read_csv("C:\\Users\\jkovacs\\Desktop\\titanic.csv")
#print(titanic.head(3))
#print(titanic.dtypes)
#titanic.to_excel("C:\\Users\\jkovacs\\Desktop\\titanic.xlsx", sheet_name="tit", index=False)
#print(titanic.info())
#ages = titanic["Age"]
#print(ages.head(3))
#print(type(ages))
#print(ages.shape)
#age_sex = titanic[["Age", "Sex"]]
#print(age_sex.head(3))
#eq_35 = titanic[titanic["Age"] == 35]
#print(eq_35.shape)
#over_35 = titanic.loc[titanic["Age"] > 35, ["Name", "Sex"]]
#print(over_35.tail(3))
#print(titanic.iloc[9:15, 2:5])
#print(titanic[["Age", "Fare"]].median())
#print(titanic[["Age", "Fare"]].describe())
#print(titanic[["Age", "Sex"]].groupby("Sex").mean())
#print(titanic.groupby("Sex")["Age"].mean())
print(titanic["Sex"].value_counts())
print(titanic.groupby(["Pclass"])["Pclass"].count())



