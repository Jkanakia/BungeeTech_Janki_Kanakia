import pandas as pd
col_list=["occupation","age"]
print(col_list)
q=pd.read_csv("main.csv",usecols=col_list)
#print(q[["occupation","age"]])
grp=q.groupby('occupation').agg({'age':['min','max']})
print(grp)

