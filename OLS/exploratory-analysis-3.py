#
# name: exploratory-analysis-3
name='exploratory-analysis-3'
description='Calculating and plotting correlation matrix'
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
## import statsmodels
#import statsmodels.formula.api as sm
#from statsmodels.graphics.correlation import plot_corr
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in0='dataframe-statsmodels.csv'
# output files
out1='data-correlation-matrix.csv'
out2='heatmap-correlation-values.jpeg'
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
print(' output 1: ',out1)
print(' output 2: ',out2)
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
# function to calculate correlation matrix and 
# write it to dataframe
#---
def calculate_correlation_matrix():
    corr = df1[:-1].corr()
    return corr
#---
# function for creating a heatmap 
# of the correlations
#---
def graph_heatmap_correlation():
    plt.figure(figsize=(8,5))
    plt.title('Heatmap Correlation Values', fontsize=16)
    #
    heat_map = sn.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    #
    plt.yticks(fontsize=5)
    plt.xticks(fontsize=5,rotation = 30)
    plt.savefig('heatmap-correlation-values.jpeg', dpi = 600)
    plt.close()
    return 
#
#-----
# main
#-----
#
# reading dataframe
df1 = read_df(input)
# calculating correlation matrix
corr = calculate_correlation_matrix()
corr.to_csv(out1, index=False, float_format='%.3f')
# graph heatmap correlation values
graph_heatmap_correlation()
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
