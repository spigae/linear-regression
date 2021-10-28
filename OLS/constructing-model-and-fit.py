#
# name: constructing-model-and-fit
name='constructing-model-and-fit'
description='Constructing the model using Ordinary Least Squares (OLS) and then fit'
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
# platform
import platform
# io
import io
# time
import time
# pandas
import pandas as pd
# import numpy
import numpy as np
# import matplotlib
import matplotlib.pyplot as plt
# import statsmodels
import statsmodels.formula.api as smf
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in1='dataframe-statsmodels.csv'
# output files
out0='fit-model.log'
out1='statistical-significance-features-with-p-values.csv'
#
# to calculate elapsed time
start_time = time.time()
print(' ')
print('',name)
print('',description)
print(' version: ',version)
print(' Python version:', platform.python_version())
print(' ')
print(' date last revision: ',date_last_revision)
print(' author: ',author)
print(' ')
print(' Inputs:')
print(' input 1: ',in1)
print(' ')
print(' Outputs:')
print(' output 0: ',out0)
print(' output 1: ',out1)
print(' ')
print(' ... script running')
print(' ')
#
#---
# function for reading the dataframe for statsmodels
#---
def read_df(filename):
    df1 = pd.read_csv(in1, sep=',')
    return df1
#---
# function to construct and fit the model
#---
def construct_fit_model():
    # creating a formula string for using in the statsmodels.OLS()
    formula_str = df1.columns[-1]+' ~ '+'+'.join(df1.columns[:-1])
    # setting the model
    model=smf.ols(formula=formula_str, data=df1)
    # fit the model
    fitted = model.fit()
    # summary of the model 
    summary_fit = fitted.summary()
    # writing to file the summary of the model
    text_file = open(out0, "w")
    # please not the presence of str: this is used to make
    # possible to write to file the summary
    text_file.write(str(summary_fit))
    text_file.close()
    return formula_str,model,fitted
#---
# function to assign Yes/No to values statistical significance 
# (using p-values) to the features
#---
def yes_no(b):
    threshold=0.05
    if b < threshold:
        return 'Yes'
    else:
        return 'No'
#---
# creating dataframe with p-values of the features
#---
def create_dataframe_results():
    df_result = pd.DataFrame()
    # p-values
    df_result['pvalues']=fitted.pvalues[1:]
    # assigning name to the column
    df_result['Features']=df1.columns[:-1]
    df_result.set_index('Features',inplace=True)
    df_result['Statistically significant?']= df_result['pvalues'].apply(yes_no)
    return df_result
#
#-----
# main
#-----
#
# reading dataframe
df1 = read_df(input)
# constructing and fitting model
formula_str,model,fitted = construct_fit_model()
# creating dataframe with p-values
df_result = create_dataframe_results()
df_result.to_csv(out1)
#
# elapsed time for the calculations
end_time = time.time()
elapsed_time = end_time - start_time
formatted_time = "{:.2f}".format(elapsed_time)
print(' Elapsed time:', formatted_time, 's')
#
print(' ')
print(' Done!')
print(' ')
print(' Please see the output files')
print(' for further information')
print(' ')
