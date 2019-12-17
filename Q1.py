import sys
import pandas as pd
df=pd.read_csv((sys.argv)[1],header=None)   #this will import the csv file without making the first row as column names
l=[]
for i in range(len(df)):                 #
    temp=[]
    for j in range(len(list(df.iloc[i]))):
        if type(list(df.iloc[i])[j]) is not float:   #this eliminates the cells contaning NaN values
            temp.append(list(df.iloc[i])[j])
    l.append(temp)
import itertools
x=list(itertools.product(*l))     #this will return all posible permutations of all rows of dataframe
result=[]
for i in range(len(x)):        #iterate to all posible permutation list and convert it to strings
    str=""
    result.append(str.join(x[i]))  
print(*result,sep=', ')
