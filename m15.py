import pandas as pd
d={"name":["aksh","el","pavi"],"marks":[55,79,80]}

p=pd.DataFrame(d)
print(p)
p.set_index("name ",inplace=True)
print(p)
print(p.describe())
print(p.loc["el"])
print(p["pavi"])
p["average"]=[["marks"]].mean(axis=1)
p.to_csv("s.csv",index=True)