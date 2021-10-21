import pandas as pd
column=["Team","Yellow Cards","Red Cards"]
data=pd.read_csv("q3.csv",usecols=column)
#print(data[["Team","Yellow Cards", "Red Cards"]])
yellow=data.sort_values(["Yellow Cards"],ascending=[False])
red=yellow.sort_values(["Red Cards"],ascending=[False])
print(red[['Team','Yellow Cards','Red Cards']])
