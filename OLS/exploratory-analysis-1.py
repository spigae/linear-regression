#
# name: exploratory-analysis-1
name='exploratory-analysis-1'
description='Evaluating the relationship between predictors and response'
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
in0='dataframe-statsmodels.csv'
#
out1='relationship-predicting-values-response-*.jpeg'
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
def read_df(filename):
    #
    df1 = pd.read_csv(in0, sep=',')
    #
    return df1
#---
# function for creating graphs of
# relationship between 
# predicting values and response
#---
def graph_relationship_predicting_values_response():
    i = 0
    for c in df1.columns[:-1]:
        i += 1
        plt.figure(figsize=(8,5))
        plt.title("{} vs. y".format(c),fontsize=16)
        plt.scatter(x=df1[c],y=df1['y'],color='blue',edgecolor='k')
        plt.grid(True)
        plt.xlabel(c,fontsize=14)
        plt.ylabel('y',fontsize=14)
        plt.savefig('relationship-predicting-values-response-' + str(i) + '.jpeg', dpi = 600)
        plt.close()
    return 
#
#-----
# main
#-----
#
# reading dataframe
df1 = read_df(input)
# creating graphs
graph_relationship_predicting_values_response()
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
