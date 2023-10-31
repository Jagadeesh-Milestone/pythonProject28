#dataframe:
import pandas as pd

details={
    'fruits':['mango','apple','banana'],
    'cost/kg':[50,120,40]
}
x=pd.DataFrame(details,index=['item1','item2','item3'])
print(x)
print(x.loc['item1'])
print(x.loc['item2'])
