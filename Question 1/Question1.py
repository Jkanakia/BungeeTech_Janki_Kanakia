import pandas as pd
data=pd.read_csv("q1.csv")
tot= data.loc[:, ~data.columns.isin(['Total'])]
grp=data.groupby((data['Year']//10)*10)
ans = {"Population": "max", "Violent": "sum", "Property": "sum","Murder":"sum","Forcible_Rape":"sum","Robbery":"sum","Aggravated_assault":"sum","Burglary":"sum","Larceny_Theft":"sum","Vehicle_Theft":"sum"}
final=grp.aggregate(ans)
print(final)
