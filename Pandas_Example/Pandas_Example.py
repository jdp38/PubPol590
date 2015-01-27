from pandas import Series, DataFrame
import pandas as pd
import numpy as np

## IMPORTING DATA ---------------------------------------------------
## assigning file paths
main_dir = "C:\Users\Daniel\Documents\GitHub\PubPol590\Pandas_Example"
csv_file = "\Data\sample_data_clean.csv"
txt_file = "\Data\sample_data_clean.txt"

## full paths to files
## type in a letter and then hit "tab" to get auto-complete feature
main_dir + csv_file
main_dir + txt_file

## importing dataframes
## read_csv (automatically sets "," as delimiter) and read_table
df = pd.read_csv(main_dir + csv_file)
df2 = pd.read_table(main_dir + txt_file)

## check object type
type(df)

## EXPLORING DATAFRAME ----------------------------------------------
list(df) # shows names of columns in dataframe
list(df2)

## extracting columns of data (series)
c = df.consump
c2 = df['consump']
type(c)

## Boolean (Logical) Operators -------------------------------------
## Comparing 2+ objects of the same type
c == c2 
c != c2
c > c2 
c >= c2

## Row Extraction----------------------------------------------------

## row slicing from dataframe
df[5:10] # df[m:n] yields rows m to n-1
df[0:10]
df[:10]
df[0:10] == df[:10]
df[10:11] # extracting a single row

## row slicing from series
c[5:10]
df.consump[5:10]

## extraction by boolean indexing
df.panid == 4
df[df.panid ==4] # extract subset of df where panid == 4
df[df.consump > 2]
df.panid[df.panid > 2]