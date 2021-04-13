import pandas as pd
import plotly.figure_factory as pf
import csv
import statistics
with open('txt/SomeRandomFile.csv') as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
file1=pd.read_csv('txt/SomeRandomFile.csv')
fig1=pf.create_distplot([file1['Avg Rating'].tolist()] , ["Average"])
fig1.show()
