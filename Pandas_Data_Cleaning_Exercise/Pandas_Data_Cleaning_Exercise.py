from pandas import Series, DataFrame
import pandas as pd
import numpy as np

main_dir = "C:\Users\Daniel\Desktop\Data"
csv_file_bad = "\sample_data_unclean.csv"
git_dir = "C:\Users\Daniel\Documents\GitHub\PubPol590"

df = pd.read_csv(main_dir + csv_file_bad)



## PYTHONG DATA TYPES ----------
## PYTHONG DATA TYPES ----------

# strings
str1 = "hello, computer"
str2 = 'hello, human'
str3 = u'eep'

type(str1) # type str
type(str2) # type str
type(str3) # type unicode

# numeric types
int1 = 10  # an integer
float1 = 20.56  # anything with a decimal
long1 = 191827319273  # for large integers

# logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)



## CREATING LISTS AND TUPLES ----------
## CREATING LISTS AND TUPLES ----------

# in brief, lists can be changed, tuples cannot.
# We will almost exclusively use lists.

list1 = []
list1
list2 = [1, 2, 3]
list2[2] # output yields 3

# tuples (remember can't be changed).
tupl1 = (8, 3, 19)
tupl1[2] # outputs is 19

#convert tupl to list
list2 = list(tupl1)
list2

# lists can be 'appended'
list2.append([3, 90])
list2 # output is [8, 3, 19, [3, 90]

# lists can be 'extended'
list2 = [8, 3, 90]
list2 # output is [8, 3, 90]
list2.extend([6, 88])
len(list2) # outpule is 5 (the length of the list)
list2 # output is [8, 3, 90, 6, 88]



## CONVERTING LISTS TO SERIES AND DATAFRAMES ----------
## CONVERTING LISTS TO SERIES AND DATAFRAMES ----------

list4 = range(5,10) # range(n,m) yields a list from n to m-1
list5 = range(5) # range(m) yields list from 0 to m-1
list5 = ['q', 'r', 's', 't', 'u']

# converting lists to series
s1 = Series(list4)
s2 = Series(list5)
s1
s2


# create Dataframe from lists OR series
list7 = range(60, 65)
zip(list4, list5)
zip1 = zip(list4, list5, list7) # parenthases are for functions, brackets are for extraction
df1 = DataFrame(zip1)

df1 = DataFrame(zip1, columns = ['two','apple',':)'])
df1['apple'] # returns q,r,s,t,u in a vertical column

df3 = DataFrame(zip1, columns = [2,'apple',':)'])
df3
df3[[2,':)']][3:4] # get column '2' and ':)'. Then get row 3... returns 8, 63

# make dataframe using dict notation
df4 = DataFrame({':(' : list4, 9 : list6}) # l

# creating DataFrame from a series ONLY
df5 = pd.concat([s1,s2])