import pandas as pd
d={"name":["aksh","sas","riya"],
   "m1":[90,60,70],
   "m2":[45,50,90]}
df=pd.DataFrame(d)
print(df)

df.set_index("name",inplace=True)
print(df)
print(df.loc["aksh"])
print(df["m1"])
newname=["pavi","laksh"]
newm1=[67,40]
newm2=[90,80]

newd={"name":newname,"m1":newm1,"m2":newm2}
print(newd)

print(df.describe())

df["average"]=df[["m1","m2"]].mean(axis=1)
print(df)

sort=df.sort_values(by="name")
print(sort)

df.to_csv("pan.csv",index=True)
print("pan.csv")