from pandas import Series, DataFrame
import pandas as pd
import numpy as np

## IMPORTING DATA
# Since I'm using just one dataset, I probably don't need two variables here, but I'm doing it anyway.
main_dir = "C:\Users\Daniel\Documents\GitHub\PubPol590\Pandas_Exercise_1"
txt_file = "\File1_small.txt"

## IMPORTING DATAFRAMES
df = pd.read_table(main_dir + txt_file, sep = " ") # key step: recognizing separator is single space.

## ROW SLICING (60-99)
df[60:100]

## EXTRACTING ROWS WHERE KWH>30
list(df)  # note that variables are "materid", "time", and "kwh"
kwh = df['kwh']
df[df.kwh > 30]