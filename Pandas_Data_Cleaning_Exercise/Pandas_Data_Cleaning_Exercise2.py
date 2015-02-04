from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "C:\Users\Daniel\Desktop\Data"
csv_file = "\sample_data_unclean.csv"
git_dir = "C:\Users\Daniel\Documents\GitHub\PubPol590"

df = pd.read_csv(main_dir + csv_file)


## FOR LOOPS ---------------
## FOR LOOPS ---------------

list1 = range(10,15)
list2 = ['a','b','c']
list3 = [1, 'a', True]

# iterating over elements (for loops)
for v in list1:
    v
for v in list2:
    print(v) # will take whatever is happening inside python and print to console. Output here is 'a','b','c'.
    
for v in list2:
    print(v, type(v)) # output is '('a', <type 'str'>)', '('b', <type 'str'>)', '('c', <type 'str'>)'
    
    
# populate a list using a for loop
list1 # is all int
list4 = [] # empy list
list5 = []

for v in list1:
    v2 = v**2
    list4.extend([v2])# must use brackets with extends. can use parentheses with append.
    list5.append(v2) # appends whatever object 'as is'

[v**2 for v in list1]
list6 = [ v < 144 for v in list1]

# iterating using enumerate
list7 = [ [i, v/2] for i, v in enumerate(list1)] # returns a list for i and v/2
list1
list7
    
    
## ITERATE THROUGH A SERIES ---------------
## ITERATE THROUGH A SERIES ---------------

s1 = df['consump']
[v > 2 for v in s1]
[[i, v] for i, v in s1.iteritems()]



## ITERATE THROUGH A DATAFRAME ---------------
## ITERATE THROUGH A DATAFRAME ---------------

[v for v in df]
[df[v] for v in df]
[[i, v] for i, v in df.iteritems()]