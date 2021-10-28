#
# name: loading-describing-data.py
name='loading-describing-data'
description='Loading and describing the data'
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
#
# declaring the files of input and output
in0='../data/concrete_data/Concrete_Data.xls'
# description and info about the dataframe
out1='description-data.csv'
out2='info-data.csv'
#
# to calculate elapsed time
start_time = time.time()
#
print(' ')
print('',name)
print('',description)
print(' version: ',version)
print(' date last revision: ',date_last_revision)
print(' ')
print(' Python version:', platform.python_version())
print(' ')
print(' author: ',author)
print(' input: ',in0)
print(' ')
print(' output 1: ',out1)
print(' output 2: ',out2)
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
# function for describing the dataframe
#---
def describe_df():
    desc = df0.describe(include='all').T
    #desc = df0.describe(include='all')
    desc.fillna('NA', inplace=True)
    #
    nrows = df0.shape[0]
    ncols = df0.shape[1] 
    return desc,nrows,ncols
#---
# function for getting information about the dataframe
#---
def info_df():
    # from :
    # https://stackoverflow.com/questions/59596498/how-to-combine-python-dataframes-info-output-with-unique-count-list
    info = []
    for col in df0.columns:
        nonNull  = len(df0) - np.sum(pd.isna(df0[col]))
        null = np.sum(pd.isna(df0[col]))
        unique = df0[col].nunique()
        colType = str(df0[col].dtype)

        info.append([col, nonNull, null, unique, colType])
    info = pd.DataFrame(info)   
    info.columns = ['colName','non-null values', 'null values', 'unique', 'dtype']
    return info
#
#-----
# main
#-----
#
# reading dataframe
df0 = read_df_excel(input)
# describing the dataframe
desc,nrows,ncols = describe_df()
desc.to_csv(out1, index=True)
print(' This dataframe is made of')
print(' # rows:',nrows)
print(' # columns:',ncols)
# information about the dataframe
info = info_df()
info.to_csv(out2, index=False)
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
