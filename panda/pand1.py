import pandas as pd,numpy as np
df=pd.date_range("20211102",periods=6)
print(df)
d=pd.DataFrame(np.random.randn(6,4),columns=['a','b','c','d'])
print(d)
print(d.loc[1])
ds={'car':[1,2,3],'bike':[8,9,7]}
p=pd.DataFrame(ds)
print(p)
s=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s['c'])
