#
# name: make-predictions.py
name='make-predictions'
description='Making prediction values from a model'
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
# import scipy
from scipy.stats import shapiro
from scipy.stats import normaltest
# import matplotlib
import matplotlib.pyplot as plt
# import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.stats.outliers_influence import OLSInfluence
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in0='../data/concrete_data/Concrete_Data.xls'
in1='../data/concrete_data/concrete_data_random_rows_for_predictions.csv'
# output files
out0='fit-model.log'
out1='predictions.csv'
#
# to calculate elapsed time
start_time = time.time()
# printing to screen
print(' ')
print('',name)
print(' version: ',version)
print('',description)
print(' date last revision: ',date_last_revision)
print(' author: ',author)
print(' Python version:', platform.python_version())
print(' ')
print(' Inputs:')
print(' input 0: ',in0)
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
# function for reading the dataframe 
# written in excel 
# it is needed to know the real name of
# variables
#---
def read_df_excel(filename):
    df0 = pd.read_excel(in0,sheet_name='Sheet1')
    # manipulating dataframe
    # making a copy of the dataframe 
    df1 = df0.copy()
    # transforming dataframe
    df1.columns=['x'+str(i) for i in range(1,9)]+['y']
    return df0,df1
#---
# function for reading the dataframe to do the predictions
#---
def read_df_for_predictions(filename):
    df2 = pd.read_csv(in1, sep=',')
    # manipulating dataframe
    # making a copy of the dataframe
    df3 = df2.copy()
    df3.columns=['x'+str(i) for i in range(1,9)]
    df2 = df3
    return df2
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
# function to make the predictions
#---
def make_predictions():
    # making the predictions
    prov = fitted.predict(df2)
    # concatenating the two dataframes
    pred = pd.concat([df2, prov], axis=1)
    # renaming the columns
    pred.columns = df0.columns
    return pred
#
#-----
# main
#-----
#
# reading dataframes (original and modified for statsmodels)
df0,df1 = read_df_excel(input)
df2 = read_df_for_predictions(input)
# constructing and fitting model
formula_str,model,fitted = construct_fit_model()
# making the predictions
predictions = make_predictions()
predictions.to_csv(out1, index=False)
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
