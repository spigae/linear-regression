#
# name: transforming.py
name='transforming'
description='Creating new dataframe for statsmodels'
# version: 0.1
version='0.1'
# date last revision: 26.10.2021
date_last_revision='26.10.2021'
# author: spigae
author='spigae'
# webpage: https://github.com/spigae
#
# importing libraries
# os
import os
# time
import time
# platform
import platform
# io
import io
# pandas
import pandas as pd
# import numpy
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
#
# declaring the files of input and output
in0='../data/concrete_data/Concrete_Data.xls'
# output files
out1='dataframe-statsmodels.csv'
#
# to calculate elapsed time
start_time = time.time()
#
print(' ')
print('',name)
print('',description)
print(' Python version:', platform.python_version())
print(' ')
print(' version: ',version)
print(' date last revision: ',date_last_revision)
print(' author: ',author)
print(' input: ',in0)
print(' ')
print(' output: ',out1)
print(' ')
print(' ... script running')
print(' ')
#
#---
# function for reading the dataframe
#---
def read_df_excel(filename):
    #
    df0 = pd.read_excel(in0,sheet_name='Sheet1')
    #
    return df0
#---
# function for creating a dataframes
# easily useable by statsmodels
#---
def manipulate_df_for_statsmodels():
    # making a copy of the dataframe
    df1 = df0.copy()
    # renaming the columns
    df1.columns=['x'+str(i) for i in range(1,len(df1.columns))]+['y']
    return df1
#
#-----
# main
#-----
#
# reading dataframe
df0 = read_df_excel(input)
# writing new dataframe
df1 = manipulate_df_for_statsmodels()
df1.to_csv(out1, index=False)
#
# elapsed time for the calculations
end_time = time.time()
elapsed_time = end_time - start_time
formatted_time = "{:.2f}".format(elapsed_time)
print(' ')
print(' Elapsed time:', formatted_time, 's')
#
print(' ')
print(' Done!')
print(' ')
print(' Please see the output files')
print(' for further information')
print(' ')
